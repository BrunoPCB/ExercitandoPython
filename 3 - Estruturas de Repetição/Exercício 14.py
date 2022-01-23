"""
14 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e 
     a quantidade de números impares.
"""

numeros = []
soma = 0
pares = 0
impares = 0

for i in range(10):
    numeros.append(input("Informe um numéro: "))
    try:
        numeros[i] = int(numeros[i])
        soma += numeros[i]

        if numeros[i]%2 == 0:
            pares += 1
        else:
            impares += 1

    except:
        print(f"Erro no {i+1}.")


print("Infomrações:"
      f"\nNúmeros:      {numeros}"
      f"\nSoma:         {soma}"
      f"\nPares:        {pares}"
      f"\nÍmpares:      {impares}")