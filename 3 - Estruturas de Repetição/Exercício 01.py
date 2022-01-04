"""
1 - Faça um programa que peça uma nota, entre zero e dez. 
    Mostre uma mensagem caso o valor seja inválido e continue 
    pedindo até que o usuário informe um valor válido.
"""

continua = True

while(continua):
    nota = input("Informe uma nota entre 0 e 10: ")

    try:
        nota = int(nota)

        if nota in range(0,11):
            print(f"O valor {nota} está entre 0 e 10.")
            continua = False
        else:
            print("O valor informa é inválido.")

    except:
        print("Valor literal inválido. Esperado valor numérico.")



