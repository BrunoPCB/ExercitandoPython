"""
10 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
     e lhe contraram para desenvolver o programa que calculará os reajustes.
        Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
        baseado no salário atual:

        salários até R$ 280,00 (incluindo) : aumento de 20%
        salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.

"""
from VerificaTipoDados import verifica_tipo_dados

salario_colaborador = input("Informe o seu salário: ")

if verifica_tipo_dados(salario_colaborador) == 1:
    salario_colaborador = float(salario_colaborador)
elif verifica_tipo_dados(salario_colaborador) == 2:
    salario_colaborador = int(salario_colaborador)
elif verifica_tipo_dados(salario_colaborador) == 999:
    print("Erro na verificação de tipo de dados.")

if salario_colaborador <= 280:

    total_aumento = (20 / 100)
    reajuste = salario_colaborador * total_aumento

elif salario_colaborador > 280 and salario_colaborador < 700:

    total_aumento = (15 / 100)
    reajuste = salario_colaborador * total_aumento

elif salario_colaborador > 700 and salario_colaborador < 1500:

    total_aumento = (10 / 100)
    reajuste = salario_colaborador * total_aumento

else:

    total_aumento = (5 / 100)
    reajuste = salario_colaborador * total_aumento


novo_salario = salario_colaborador + reajuste

print("\nReajuste salarial")
print(f"Salário do colaborador: R${salario_colaborador:.2f}\n"
      f"Aumento(percentual): {total_aumento * 100}%\n"
      f"Valor do reajuste: R${reajuste:.2f}\n"
      f"Salário + Aumento: R${novo_salario:.2f}.")

