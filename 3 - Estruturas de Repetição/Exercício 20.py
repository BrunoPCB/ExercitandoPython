"""
20 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e 
limitando o fatorial a números inteiros positivos e menores que 16.
"""

continuar = True

while(continuar):

    n = input("Informe um número inteiro, e mostraremos seu fatorial: ")
    total = 1

    try:
        n = int(n)

        if 0 < n < 16:
            for i in range(n, 0, -1):
                total *= i

            print(total)
        else:
            print("O valor informado deve ser mais que 0 e menor que 16.")
    except:
        print("Erro, tipo de dado informado inválido.")

    if total != 1:
        fim = input("{[n] Para Sair }\n"
                    "Deseja continuar? ")
        if fim.upper() in ["N", "NÃO", "NAO"]:
            continuar = False


    