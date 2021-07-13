"""
25 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:

        Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro

        Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro

        Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
        (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a
        ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço
        do litro do álcool é R$ 1,90.
"""

combustivel = {"A": 1.90, "G": 2.50}
tipo_combustivel = ''

try:
    tipo_combustivel = input("Escolha o combustível:\n"
                             "(1) Álcool\n"
                             "(2) Gasolina\n")

    if tipo_combustivel == '1':
        tipo_combustivel = "A"
    elif tipo_combustivel == '2':
        tipo_combustivel = "G"

except IndexError as e:
    print("Número informado está fora do alcance.")


quantidade_litros = int(input("Informe a quantidade de litros: "))

preco_combustivel, desconto, preco = 0, 0, 0

if quantidade_litros <= 20:
    preco_combustivel = combustivel[tipo_combustivel] * quantidade_litros
    desconto = preco_combustivel * 0.03
    preco = preco_combustivel - desconto

if quantidade_litros > 20:
    preco_combustivel = combustivel[tipo_combustivel] * quantidade_litros
    desconto = preco_combustivel * 0.04
    preco = preco_combustivel - desconto

print(f"\n - - - Nota Fiscal - - - \n"
      f"Combustível: {'Gasolina' if tipo_combustivel == 'G' else 'Ácool'}\n"
      f"Preço p/ Litro: {combustivel[tipo_combustivel]}\n"
      f"Preço combustível: {preco_combustivel}\n"
      f"Desconto: {desconto}\n"
      f"---------------------------------\n"
      f"Total: {preco}")
