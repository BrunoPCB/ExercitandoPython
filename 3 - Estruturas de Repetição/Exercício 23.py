"""
23 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
     O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
     Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""
from secrets import randbelow


numero = input("Informe um valor para N: ")
primos = []
conta_divisoes = 0

try:
    numero = int(numero)
    
    for i in range(1, numero+1):
        cont = 0
        for j in range(1, i+1):
            if i % j == 0:
                cont += 1
        
        if cont <= 2:
            primos.append(i)
            conta_divisoes += cont


except ValueError as ve:
    print("Erro de Valor: ", ve)
except TypeError as te:
    print("Erro de Tipo: ", te)
except Exception as e:
    print("Erro: ", e)

print(f"\nNúmeros primos entre 1 e {numero} são: \n"
      f"{primos}\n"
      f"Foram necessárias {conta_divisoes} divisões.\n")

