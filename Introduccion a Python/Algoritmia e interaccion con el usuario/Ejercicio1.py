"""Conversor de temperaturas"""

print(f"Ingrese una temperatura en Celisius: ", end="")
temperatura = float(input(""))
print(
    f"La temperatura es:\n\tFahrenheit: {temperatura * 1.8 + 32}F \n\tKelvin: {temperatura + 273.15}K"
)
