"""
10 - Faça um Programa que peça a temperatura em
graus Celsius, transforme e mostre em graus
Fahrenheit.
"""
# Receber temperatura em graus celsius.
celsius = int(input("Informe a temperatura em graus Celsius: "))

# Calculo de conversão celsius -> Farenheit
# (0 °C × 9/5) + 32
Fahrenheit = ((celsius * 9) / 5) + 32

# Mostrar conversão na tela
print(f" Celsius  ->  Fahrenheit")
print(f"{celsius}°C -> {Fahrenheit:.0f}°F")