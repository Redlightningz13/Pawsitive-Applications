package com.pawsitive.rentcalculator

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                RentCalculatorScreen()
            }
        }
    }
}

private fun buildParagraph(avgMonthlyRent: Double, weeklyCostPerUnit: Double, percent: Double): String {
    return "With average rent at $${"%,.0f".format(avgMonthlyRent)} per unit, " +
        "a weekly cost of $${"%,.2f".format(weeklyCostPerUnit)} per apartment is just " +
        "${"%.1f".format(percent)}% of monthly rent. That small investment keeps the " +
        "property consistently clean, improves resident satisfaction and reviews, " +
        "reduces vacancies, and supports higher, luxury-level rents—generating far more " +
        "value than it costs."
}

@androidx.compose.runtime.Composable
fun RentCalculatorScreen() {
    var avgRent by remember { mutableStateOf("") }
    var weeklyPrice by remember { mutableStateOf("") }
    var units by remember { mutableStateOf("") }
    var weeklyCostResult by remember { mutableStateOf("") }
    var percentResult by remember { mutableStateOf("") }
    var paragraph by remember { mutableStateOf("") }
    var error by remember { mutableStateOf("") }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Color(0xFFF5F9F4))
            .padding(16.dp)
            .verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(10.dp)
    ) {
        Text("Pawsitive Rent Calculator", style = MaterialTheme.typography.headlineSmall)

        OutlinedTextField(avgRent, { avgRent = it }, label = { Text("Average monthly rent per unit") }, modifier = Modifier.fillMaxWidth())
        OutlinedTextField(weeklyPrice, { weeklyPrice = it }, label = { Text("Weekly total price/cost") }, modifier = Modifier.fillMaxWidth())
        OutlinedTextField(units, { units = it }, label = { Text("Number of units") }, modifier = Modifier.fillMaxWidth())

        Button(onClick = {
            error = ""
            if (avgRent.isBlank() || weeklyPrice.isBlank() || units.isBlank()) {
                weeklyCostResult = ""
                percentResult = ""
                paragraph = ""
                return@Button
            }
            try {
                val avg = avgRent.toDouble()
                val weekly = weeklyPrice.toDouble()
                val numUnits = units.toInt()
                require(avg > 0 && weekly >= 0 && numUnits > 0)

                val weeklyCostPerUnit = weekly / numUnits
                val percentOfMonthly = (weeklyCostPerUnit * 4 / avg) * 100

                weeklyCostResult = "$${"%,.2f".format(weeklyCostPerUnit)}"
                percentResult = "${"%.2f".format(percentOfMonthly)}%"
                paragraph = buildParagraph(avg, weeklyCostPerUnit, percentOfMonthly)
            } catch (_: Exception) {
                error = "Enter valid values: rent > 0, units > 0, weekly price >= 0"
            }
        }) {
            Text("Calculate")
        }

        if (error.isNotBlank()) Text(error, color = Color.Red)
        if (weeklyCostResult.isNotBlank()) Text("Weekly cost per unit: $weeklyCostResult")
        if (percentResult.isNotBlank()) Text("Cost as % of monthly rent: $percentResult")
        if (paragraph.isNotBlank()) Text(paragraph, fontFamily = FontFamily.SansSerif)
    }
}
