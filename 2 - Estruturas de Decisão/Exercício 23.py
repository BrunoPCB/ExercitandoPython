"""
23 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
     O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
        par ou ímpar;
        positivo ou negativo;
        inteiro ou decimal.
"""
numero = []
resultado = 0

numero.append(float(input("Informe o primeiro número: ")))
numero.append(float(input("Informe o segundo número: ")))

print("Escolha uma das seguintes operações: \n"
      "(1) + Adição\n"
      "(2) - Subtração\n"
      "(3) / Divisão\n"
      "(4) * Multiplicação\n")

operacao = int(input("Qual sua escolha: "))

if operacao == 1:
    resultado = sum(numero)
elif operacao == 2:
    resultado = numero[1] - numero[2]
elif operacao == 3:
    resultado = numero[1] / numero[2]
elif operacao == 4:
    resultado = numero[1] * numero[2]
else:
    print("O número informado não condiz com nenhuma das opções.")

par, positivo, inteiro = False, False, False

if resultado % 2 == 0:
    par = True

if resultado > 0:
    positivo = True

if resultado / 1 == resultado:
    inteiro = True

print()
print(f"O número {resultado} é:\n"
      f"{'Par' if par else 'Ímpar'}\n"
      f"{'Positivo' if positivo else 'Negativo'}\n"
      f"{'Inteiro' if inteiro else 'Decimal'}")
