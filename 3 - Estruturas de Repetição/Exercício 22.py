"""
22 - Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, 
     por quais número ele é divisível.
"""

numero = input("Informe um número: ")
primo = False
divisiveis = []

try:
    numero = int(numero)

    cont = 0
    for j in range(1, numero+1):
        if numero % j == 0:
            cont += 1
            divisiveis.append(j)
        
    
    if cont <= 2:
        primo = True
        
except Exception as e:
    print("Error: ", e)

if primo:
    print(f"O número {numero}, é um número PRIMO.")
else:
    print(f"O número {numero}, NÃO é um número PRIMO."
          f"\nEste número é divisível por {divisiveis}.")