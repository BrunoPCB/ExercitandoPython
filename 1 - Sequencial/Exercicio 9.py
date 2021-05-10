"""
9 - Faça um Programa que peça a temperatura em
graus Fahrenheit, transforme e mostre a
temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
# Informando a temperatura em Fahrenheit
fahrenheit = int(input("Informe a temperatura? "))

# Calculo de conversão para Celsius
Celsius = 5 * ((fahrenheit - 32) / 9)

# Mostrando o resultado
print(f"{fahrenheit}°F em celsius é igual a {Celsius:.0f}°C")
