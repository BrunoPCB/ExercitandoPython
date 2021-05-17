"""
16 - Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

Area a ser pintada;
1 litro para cada 3 metros quadrados;
R$ 80,00 para cada 18 litros
Quantas latas necessárias para e seu preço para o tamanho definido pelo usuário?
"""
# Obtendo dados
AreaPintar = float(input("Área a ser pintada[m²]: "))

# Cálculos
qtdLitros   =   AreaPintar / 3
qtdLatas    =   qtdLitros / 18
precoLatas  =   qtdLatas * 80

# Imprimindo na tela
print()
print(f"Área a ser pintada: {AreaPintar:.1f}\n"
      f"Litros: {qtdLitros:.2f}\n"
      f"Latas: {qtdLatas:.2f}\n"
      f"Preço: R${precoLatas:.2f}")
