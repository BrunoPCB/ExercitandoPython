"""
26 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
        Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
        Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

        Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
        R$ 25,00, receberá ainda um desconto de 10% sobre este total.
        Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de
        maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

qtd_kg_morangos = float(input("Informe quantos Kgs de morangos você deseja: "))
qtd_kg_macas = float(input("Informe quantos Kgs de maçãs você deseja: "))

total_kg = qtd_kg_morangos + qtd_kg_macas
preco_morango, preco_maca, preco, desconto = 0, 0, 0, 0

if qtd_kg_morangos <= 5:
    preco_morango = 2.50 * qtd_kg_morangos
else:
    preco_morango = 2.20 * qtd_kg_morangos

if qtd_kg_macas <= 5:
    preco_maca = 1.80 * qtd_kg_macas
else:
    preco_maca = 1.50 * qtd_kg_macas

preco = preco_maca + preco_morango

if total_kg > 8 and preco > 25:
    desconto = preco * 0.1
    preco -= desconto

print(f"- - - - - - - Nota Fiscal - - - - - - - \n"
      f"Morangos           {qtd_kg_morangos}Kg - R${preco_morango:.2f}\n"
      f"Maçã               {qtd_kg_macas}Kg - R${preco_maca:.2f}\n"
      f"- - - - - - - - - - - - - - - - - - - - ")
if desconto > 0:
    print(f"{f'Desconto            R${desconto:.2f}'}")
print(f"Total               R${preco:.2f}\n")
