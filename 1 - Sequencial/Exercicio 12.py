"""
12 - Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal, usando
a seguinte fórmula: (72.7*altura) - 58
"""
# Recebendo os valores de entrada
altura = int(input("Qual sua altura(cm): "))

# Calculando
peso_ideal = (72.2 * (altura / 100)) - 58

# Mostrando resultado
print(f"O peso ideal para a {altura:.0f} cm altura é {peso_ideal:.2f}.")