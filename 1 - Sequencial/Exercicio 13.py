"""
13 - Tendo como dado de entrada a altura (h) de
uma pessoa, construa um algoritmo que calcule
seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
# Recebendo valores
altura = int(input("Informe a sua altura(cm): "))

# Calculando
Peso_Homens = (72.7 * (altura / 100)) - 58
Peso_Mulheres = (62.1 * (altura / 100)) - 44.7

# Mostrando resultados
print(f"Altura: {(altura / 100):.2f}m\n"
      f"Homens: {Peso_Homens:.2f}kg\n"
      f"Mulheres: {Peso_Mulheres:.2f}kg")
