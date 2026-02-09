import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk
import tkinter.font as tkfont

BACKGROUND_COLOR = "#F5F9F4"
ACCENT_COLOR = "#DCEFE1"


def calculate():
    avg_text = avg_rent_var.get().strip()
    weekly_text = weekly_price_var.get().strip()
    units_text = units_var.get().strip()

    # Allow blank fields without showing an error dialog.
    if not avg_text or not weekly_text or not units_text:
        weekly_cost_var.set("")
        monthly_percent_var.set("")
        paragraph_output.configure(state="normal")
        paragraph_output.delete("1.0", tk.END)
        paragraph_output.configure(state="disabled")
        return

    try:
        avg_monthly_rent = float(avg_text)
        weekly_total_price = float(weekly_text)
        number_of_units = int(units_text)

        if avg_monthly_rent <= 0 or weekly_total_price < 0 or number_of_units <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Invalid input",
            "Please enter positive numbers for average rent and unit count, and a non-negative weekly price.",
        )
        return

    weekly_cost_per_unit = weekly_total_price / number_of_units
    percent_of_monthly_rent = (weekly_cost_per_unit * 4 / avg_monthly_rent) * 100

    weekly_cost_var.set(f"${weekly_cost_per_unit:,.2f}")
    monthly_percent_var.set(f"{percent_of_monthly_rent:.2f}%")

    paragraph = (
        f"With average rent at ${avg_monthly_rent:,.0f} per unit, "
        f"a weekly cost of ${weekly_cost_per_unit:,.2f} per apartment is just "
        f"{percent_of_monthly_rent:.1f}% of monthly rent. That small investment keeps the "
        f"property consistently clean, improves resident satisfaction and reviews, "
        f"reduces vacancies, and supports higher, luxury-level rents—generating far more "
        f"value than it costs."
    )

    paragraph_output.configure(state="normal")
    paragraph_output.delete("1.0", tk.END)
    paragraph_output.insert(tk.END, paragraph)
    paragraph_output.configure(state="disabled")


def update_fonts(_event=None):
    width_scale = root.winfo_width() / 900
    height_scale = root.winfo_height() / 650
    scale = max(0.9, min(1.8, min(width_scale, height_scale)))

    heading_font.configure(size=max(16, int(20 * scale)))
    label_font.configure(size=max(10, int(11 * scale)))
    value_font.configure(size=max(12, int(13 * scale)))
    button_font.configure(size=max(10, int(11 * scale)))
    paragraph_font.configure(size=max(11, int(12 * scale)))


def load_logo():
    candidates = ["pawsitive_logo.png", "logo.png", "pawsitive.png"]

    for candidate in candidates:
        image_path = Path(candidate)
        if image_path.exists():
            img = tk.PhotoImage(file=str(image_path))
            shrink_factor = max(1, img.width() // 180)
            logo = img.subsample(shrink_factor, shrink_factor)
            logo_label.configure(image=logo, text="")
            logo_label.image = logo
            return

    logo_label.configure(text="PAWSITIVE", font=("Segoe UI", 18, "bold"), fg="#34423D")


root = tk.Tk()
root.title("Rent Value Calculator")
root.geometry("900x650")
root.minsize(760, 540)
root.configure(bg=BACKGROUND_COLOR)

heading_font = tkfont.Font(family="Segoe UI", size=20, weight="bold")
label_font = tkfont.Font(family="Segoe UI", size=11)
value_font = tkfont.Font(family="Segoe UI", size=13, weight="bold")
button_font = tkfont.Font(family="Segoe UI", size=11)
paragraph_font = tkfont.Font(family="Segoe UI", size=12)

style = ttk.Style()
style.theme_use("clam")
style.configure("Panel.TLabelframe", background=ACCENT_COLOR, bordercolor=ACCENT_COLOR)
style.configure("Panel.TLabelframe.Label", background=ACCENT_COLOR, font=("Segoe UI", 11, "bold"))
style.configure("Panel.TLabel", background=ACCENT_COLOR, font=("Segoe UI", 11))
style.configure("Main.TLabel", background=BACKGROUND_COLOR)
style.configure("Main.TButton", font=("Segoe UI", 11, "bold"))

main = tk.Frame(root, bg=BACKGROUND_COLOR, padx=20, pady=20)
main.pack(fill="both", expand=True)
main.grid_columnconfigure(0, weight=1)
main.grid_rowconfigure(3, weight=1)

header_frame = tk.Frame(main, bg=BACKGROUND_COLOR)
header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 12))
header_frame.grid_columnconfigure(0, weight=1)

header = ttk.Label(
    header_frame,
    text="Property Cost-to-Rent Value Calculator",
    style="Main.TLabel",
    font=heading_font,
)
header.grid(row=0, column=0, sticky="w")

logo_label = tk.Label(header_frame, bg=BACKGROUND_COLOR)
logo_label.grid(row=0, column=1, sticky="e")
load_logo()

avg_rent_var = tk.StringVar()
weekly_price_var = tk.StringVar()
units_var = tk.StringVar()
weekly_cost_var = tk.StringVar(value="")
monthly_percent_var = tk.StringVar(value="")

input_panel = ttk.LabelFrame(main, text="Inputs", padding=14, style="Panel.TLabelframe")
input_panel.grid(row=1, column=0, sticky="ew", pady=(0, 10))
input_panel.columnconfigure(1, weight=1)

fields = [
    ("Average monthly rent per unit ($)", avg_rent_var),
    ("Weekly price you are charging/property cost ($)", weekly_price_var),
    ("Number of units", units_var),
]

for idx, (text, variable) in enumerate(fields):
    ttk.Label(input_panel, text=text, style="Panel.TLabel", font=label_font).grid(
        row=idx, column=0, sticky="w", pady=6, padx=(0, 10)
    )
    ttk.Entry(input_panel, textvariable=variable).grid(row=idx, column=1, sticky="ew", pady=6)

button_row = tk.Frame(main, bg=BACKGROUND_COLOR)
button_row.grid(row=2, column=0, sticky="ew", pady=(0, 10))

calc_btn = ttk.Button(button_row, text="Calculate", command=calculate, style="Main.TButton")
calc_btn.pack(side="left")

close_btn = ttk.Button(button_row, text="Close Window", command=root.destroy, style="Main.TButton")
close_btn.pack(side="right")

content_frame = tk.Frame(main, bg=BACKGROUND_COLOR)
content_frame.grid(row=3, column=0, sticky="nsew")
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_rowconfigure(1, weight=1)

results = ttk.LabelFrame(content_frame, text="Results", padding=12, style="Panel.TLabelframe")
results.grid(row=0, column=0, sticky="ew", pady=(0, 10))
results.columnconfigure(1, weight=1)

ttk.Label(results, text="Weekly cost per unit:", style="Panel.TLabel", font=label_font).grid(
    row=0, column=0, sticky="w", pady=4
)
ttk.Label(results, textvariable=weekly_cost_var, style="Panel.TLabel", font=value_font).grid(
    row=0, column=1, sticky="w", pady=4
)

ttk.Label(results, text="Cost as % of monthly rent:", style="Panel.TLabel", font=label_font).grid(
    row=1, column=0, sticky="w", pady=4
)
ttk.Label(results, textvariable=monthly_percent_var, style="Panel.TLabel", font=value_font).grid(
    row=1, column=1, sticky="w", pady=4
)

paragraph_frame = ttk.LabelFrame(content_frame, text="Generated Paragraph", padding=12, style="Panel.TLabelframe")
paragraph_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 14))
paragraph_frame.grid_columnconfigure(0, weight=1)
paragraph_frame.grid_rowconfigure(0, weight=1)

paragraph_output = tk.Text(
    paragraph_frame,
    wrap="word",
    padx=10,
    pady=10,
    font=paragraph_font,
    bg="white",
    relief="flat",
)
paragraph_output.grid(row=0, column=0, sticky="nsew", pady=(0, 8))
paragraph_output.configure(state="disabled")

root.bind("<Configure>", update_fonts)
calculate()
root.mainloop()
