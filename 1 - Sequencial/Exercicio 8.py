"""
8 - Faça um Programa que pergunte quanto você ganha
por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
# Recebe o valor que o usuário recebe trabalhando por hora.
salario = float(input("Quanto você ganha por hora? "))

# Cálculo de quanto o usuário recebe por mês
salario_por_mes = salario * 30

# Mostrando na tela o resultado.
print(f"O seu salário, recebendo R${salario:.2f}/H é de R${salario_por_mes:.2f}.")