"""
11 - Faça um Programa que peça 2 números inteiros
e um número real. Calcule e mostre:
 - o produto do dobro do primeiro
   com metade do segundo .
 - a soma do triplo do primeiro
   com o terceiro.
 - o terceiro elevado ao cubo.

Neste caso no qual os calculos já estão definidos e o código
segue de forma sequencial podemos pedir para o programa
realiar os cálculos de uma só vez, porém para melhor
uso do processamento.
"""
# Pedindo os valores
int_1 = int(input("Primeiro valor inteiro: "))
int_2 = int(input("Segundo valor inteiro: "))
float_1 = float(input("Primeiro valor real: "))

# Calculos

# Primeiro: (int_1 * 2) *  (int_2 / 2)
calculo_1 = (int_1 * 2) *  (int_2 / 2)

# Segundo: (int_1 * 3) + float_1
calculo_2 = (int_1 * 3) + float_1

# Terceiro: float_1³
calculo_3 = pow(float_1, 3)

#Mostrando resultados
print(f"O produto do dobro do primeiro com metade do segundo: {calculo_1:.2f}")
print(f"A soma do triplo do primeiro com o terceiro: {calculo_2:.2f}")
print(f"O terceiro elevado ao cubo: {calculo_3:.2f}")