import tkinter as tk
from tkinter import ttk, messagebox


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
        weekly_cost_var.set("")
        monthly_percent_var.set("")
        paragraph_output.configure(state="normal")
        paragraph_output.delete("1.0", tk.END)
        paragraph_output.configure(state="disabled")
        messagebox.showerror(
            "Invalid input",
            "Please enter positive numbers for average rent and unit count, and a non-negative weekly price.",
        )
        return

    weekly_cost_per_unit = weekly_total_price / number_of_units
    # Convert weekly cost to calendar-month equivalent: 52 weeks / 12 months.
    monthly_cost_per_unit = weekly_cost_per_unit * (52 / 12)
    percent_of_monthly_rent = (monthly_cost_per_unit / avg_monthly_rent) * 100

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


root = tk.Tk()
root.title("Rent Value Calculator")
root.geometry("760x500")
root.resizable(False, False)

main = ttk.Frame(root, padding=16)
main.pack(fill="both", expand=True)

header = ttk.Label(
    main,
    text="Property Cost-to-Rent Value Calculator",
    font=("Segoe UI", 16, "bold"),
)
header.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 16))

avg_rent_var = tk.StringVar(value="1300")
weekly_price_var = tk.StringVar(value="250")
units_var = tk.StringVar(value="171")
weekly_cost_var = tk.StringVar(value="")
monthly_percent_var = tk.StringVar(value="")

fields = [
    ("Average monthly rent per unit ($)", avg_rent_var),
    ("Weekly price you are charging/property cost ($)", weekly_price_var),
    ("Number of units", units_var),
]

for idx, (label, var) in enumerate(fields, start=1):
    ttk.Label(main, text=label).grid(row=idx, column=0, sticky="w", pady=6)
    ttk.Entry(main, textvariable=var, width=28).grid(row=idx, column=1, sticky="w", pady=6)

calc_btn = ttk.Button(main, text="Calculate", command=calculate)
calc_btn.grid(row=4, column=0, sticky="w", pady=(12, 8))

results = ttk.LabelFrame(main, text="Results", padding=12)
results.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(8, 8))

results.columnconfigure(1, weight=1)

ttk.Label(results, text="Weekly cost per unit:").grid(row=0, column=0, sticky="w", pady=4)
ttk.Label(results, textvariable=weekly_cost_var, font=("Segoe UI", 11, "bold")).grid(
    row=0, column=1, sticky="w", pady=4
)

ttk.Label(results, text="Cost as % of monthly rent:").grid(row=1, column=0, sticky="w", pady=4)
ttk.Label(results, textvariable=monthly_percent_var, font=("Segoe UI", 11, "bold")).grid(
    row=1, column=1, sticky="w", pady=4
)

paragraph_frame = ttk.LabelFrame(main, text="Generated Paragraph", padding=12)
paragraph_frame.grid(row=6, column=0, columnspan=2, sticky="nsew", pady=(8, 0))

paragraph_output = tk.Text(paragraph_frame, wrap="word", height=8, width=86)
paragraph_output.pack(fill="both", expand=True)
paragraph_output.configure(state="disabled")

calculate()

root.mainloop()
