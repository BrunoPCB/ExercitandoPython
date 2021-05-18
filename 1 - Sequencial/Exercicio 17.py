"""
17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

"""


# Recebendo valores
area_pintar = float(input("Tamanho em metros quadrados da área a ser pintada: "))

# Cálculos
qtd_litros   = area_pintar / 6

qtd_latas    = round((qtd_litros / 18) + 0.5)
preco_latas  = qtd_latas * 80

qtd_galoes   = round((qtd_litros / 3.6) + 0.5)
preco_galoes = qtd_galoes * 25

# Imprimindo
print("- - - - Dados - - - -\n"
      f"Área: {area_pintar:.1f}m²\n"
      f"Litros: {qtd_litros:.2f}L\n")

print("Comprando latas de 18 litros")
print(f"Total de latas: {qtd_latas:.0f} latas\n"
      f"Preço: R${preco_latas:.2f}\n")

print("Comprando galões de 3,6 litros")
print(f"Total de galões: {qtd_galoes:.0f} galões\n"
      f"Preço: R${preco_galoes:.2f}\n")

# Usando estruturas de decisão
if qtd_litros > 18:
    qtd_latas   = round((qtd_litros // 18) + 0.5)
    qtd_galoes  = round(((qtd_litros - (qtd_latas * 18)) / 3.6) + 0.5)
else:
    qtd_latas = 0
    qtd_galoes = round((qtd_litros / 3.6) + 0.5)
# Usando estruturas de decisão

print("Comprando galões e latas")
print(f"Latas: {qtd_latas:.0f} lata(s)\n"
      f"Galões: {qtd_galoes:.0f} galão(ões)")
