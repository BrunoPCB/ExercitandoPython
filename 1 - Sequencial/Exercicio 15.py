"""
15 - Faça um Programa que pergunte quanto você ganha por
hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de
Renda, 8% para o INSS e 5% para o sindicato, faça um
programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
# Recebendo valores
salario = float(input("Quanto você ganha por hora: "))
horas_trabalhadas = int(input("Quantidade de horas trabalhadas no mês: "))

# Cálculos
salario_mensal = salario * horas_trabalhadas
impostos = salario_mensal * 11 / 100
inss = salario_mensal * 8 / 100
sindicato = salario_mensal * 5 / 100
salario_mensal_descontos = salario_mensal - impostos - inss - sindicato

# Mostrando informações
print(10 * "----")
print(f"Salário por hora: R${salario:.2f}\n"
      f"Horas trabalhadas: {horas_trabalhadas} horas\n"
      f"Salário mensal: R${salario_mensal:.2f}\n"
      f"Impostos: R${impostos:.2f}\n"
      f"Inss: R${inss:.2f}\n"
      f"Sindicato: R${sindicato:.2f}\n"
      f"Salário com descontos: R${salario_mensal_descontos:.2f}")
print(10 * "----")