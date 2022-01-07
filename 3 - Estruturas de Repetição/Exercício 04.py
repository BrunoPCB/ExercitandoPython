"""
4 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma 
    taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com 
    uma taxa de crescimento de 1.5%. 
    Faça um programa que calcule e escreva o número de anos necessários para que a 
    população do país A ultrapasse ou iguale a população do país B, mantidas as 
    taxas de crescimento.
"""

pais = [80000, 200000]

anos = 0

crescimento_anual_A = pais[0] * (3/100)
crescimento_anual_B = pais[0] * (1.5/100)

while(pais[0] != pais[1]):
    pais[0] = pais[0] + crescimento_anual_A
    pais[1] = pais[1] + crescimento_anual_B

    anos += 1


print(f"O país A precisará de {anos} anos para se igualar com o país B.")
