"""
6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
# Pedindo o raio do círculo -> raio = diâmetro/2
raio = int(input("Informe o raio do círculo: "))
pi = 3.1415

# Calculando área do círculo
area_circulo = float((pow(raio, 2)) * pi)

# Imprimindo resultado
print(f"A área do círculo de raio {raio} é {area_circulo:.2f}.")