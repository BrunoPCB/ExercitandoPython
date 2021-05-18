"""
3  - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
letra = input("Digite uma F, para Feminino e M, para Masculino: ")

if letra == 'F' or letra == 'f':
    print("FEMININO")
elif letra == 'M' or letra == 'm':
    print("MASCULINO")
else:
    print("A letra informada não condiz com as opções informadas.")
