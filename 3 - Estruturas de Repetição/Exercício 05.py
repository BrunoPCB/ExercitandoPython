"""
5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
    Valide a entrada e permita repetir a operação.
"""


pais = [0, 0]

for i in range(2):
    pais[i] = input(f"Infome o valor de Habitantes para o País {i+1}: ")
    try:
        pais[i] = float(pais[i])
    except:
        print("Erro")


anos = 0

crescimento_anual_A = pais[0] * (3/100)
crescimento_anual_B = pais[0] * (1.5/100)

while(pais[0] != pais[1]):
    pais[0] = pais[0] + crescimento_anual_A
    pais[1] = pais[1] + crescimento_anual_B

    anos += 1


if pais[0] >= pais[1]:
    print(f"O país A precisará de {anos} anos para se igualar com o país B.")
else:
    print(f"O país B precisará de {anos} anos para se igualar com o país A.")