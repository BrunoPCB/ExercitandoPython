"""
24 - Faça um programa que calcule o mostre a média aritmética de N notas.
"""

qtd_notas = input("Informe a quantidade de notas: ")
notas = []
media = 0

try:
    qtd_notas = int(qtd_notas)

    for i in range(qtd_notas):
        notas.append(input(f"Informe a {i+1}ª nota: "))
        try: notas[i] = int(notas[i]) 
        except Exception as e:
            print("Erro notas: ", e)

    for valor in notas:
        media += valor
    
    media /= len(notas)

except Exception as e:
    print(e)


print("\nA média aritimética entre as seguintes notas:\n"
      f"{notas}\n"
      f"É igual a: {media:.2f}.\n")

