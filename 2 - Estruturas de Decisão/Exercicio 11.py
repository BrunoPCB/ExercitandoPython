"""
11 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
     que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11%
     do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário
     Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
     trabalhadas no mês.
     Desconto do IR:
        Salário Bruto até 900 (inclusive) - isento
        Salário Bruto até 1500 (inclusive) - desconto de 5%
        Salário Bruto até 2500 (inclusive) - desconto de 10%
        Salário Bruto acima de 2500 - desconto de 20%
        Imprima na tela as informações, dispostas conforme o exemplo abaixo.
        No exemplo o valor da hora é 5 e a quantidade de hora é 220.
                Salário Bruto: (5 * 220)        : R$ 1100,00
                (-) IR (5%)                     : R$   55,00
                (-) INSS ( 10%)                 : R$  110,00
                FGTS (11%)                      : R$  121,00
                Total de descontos              : R$  165,00
                Salário Liquido                 : R$  935,00

"""
from VerificaTipoDados import verifica_tipo_dados


def calcular_descontos(sal, imposto_renda_calc):
    inss_calc = sal * (10 / 100)
    fgts_calc = sal * (11 / 100)
    total_descontos_calc = imposto_renda_calc + inss_calc
    calc_salario_liquido_funcionario = sal - total_descontos_calc + fgts_calc - imposto_renda
    return inss_calc, fgts_calc, total_descontos_calc, calc_salario_liquido_funcionario


valor_hora = input("Informe valor por hora: ")
total_hora = input("Informe horas trabalhadas: ")

verifica_valor_hora = verifica_tipo_dados(valor_hora)
verifica_total_hora = verifica_tipo_dados(total_hora)

if verifica_valor_hora == 1:  # Float
    valor_hora = float(valor_hora)
elif verifica_valor_hora == 2:  # Int
    valor_hora = int(valor_hora)
elif verifica_valor_hora == 999:  # Erro
    print("Erro na verificação do tipo de Dados.")

if verifica_total_hora == 1:  # Float
    total_hora = float(total_hora)
elif verifica_total_hora == 2:  # Int
    total_hora = int(total_hora)
elif verifica_total_hora == 999:  # Erro
    print("Erro na verificação do tipo de Dados.")

salario_bruto_funcionario = valor_hora * total_hora

if salario_bruto_funcionario < 900:  # Isento
    desc = 0
    imposto_renda = 0
    inss, fgts, total_descontos, salario_liquido_funcionario = calcular_descontos(salario_bruto_funcionario, imposto_renda)
elif 900 < salario_bruto_funcionario <= 1500:  # Desconto de 5%
    desc = 5
    imposto_renda = salario_bruto_funcionario * 5 / 100
    inss, fgts, total_descontos, salario_liquido_funcionario = calcular_descontos(salario_bruto_funcionario, imposto_renda)
elif 1500 < salario_bruto_funcionario <= 2500:  # Desconto de 10%
    desc = 10
    imposto_renda = salario_bruto_funcionario * 10 / 100
    inss, fgts, total_descontos, salario_liquido_funcionario = calcular_descontos(salario_bruto_funcionario, imposto_renda)
else:  # Desconto de 20%
    desc = 20
    imposto_renda = salario_bruto_funcionario * 20 / 100
    inss, fgts, total_descontos, salario_liquido_funcionario = calcular_descontos(salario_bruto_funcionario, imposto_renda)

print()
print("Folha de Pagamento")
print("Salário Bruto: ",    5 * " ", f"R${salario_bruto_funcionario:.2f}\n"
      f"( - {desc}% )IR:", 8 * " ", f"R${imposto_renda:.2f}\n"
      "( - 10% )INSS: ",    5 * " ", f"R${inss:.2f}\n"
      "( + 11% )FGTS: ",    5 * " ", f"R${fgts:.2f}\n"
      "Total descontos: ",  3 * " ", f"R${total_descontos:.2f}\n"
      "Salário líquido: ",  3 * " ", f"R${salario_liquido_funcionario:.2f}")
