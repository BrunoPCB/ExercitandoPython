"""
Objetivo: Verificar tipo de dados do valor recebido;

Descrição: Esse código tem como finalidade fazer a verificação de tip de dados que o usuáro digitou,
assim que ele digitar veremos a melhor opção para modificar o tipo de dados da variável.
"""


def verifica_tipo_dados(variavel):
    if variavel.isalpha():
        #print("Valor é alfabético.")
        return 0
    else:
        try:
            variavel = float(variavel)  # Float que obtem valor, seja inteiro, seja ponto flutuante.
            if not variavel.is_integer():
                #print("É float")
                #variavel = float(variavel)
                return 1
            else:
                #print("Não é float")
                #variavel = int(variavel)
                return 2
        except:
            print("Não deu certo")
            return 999

"""
Alfa-númericos = isalnum, isalpha, isdecimal, isdigit

    isalnum -> Valores alfabéticos e númericos.
    isalnum: 'a-z', 'A-Z', 0-infinito, (-0)-(-infinito)
    Exemplo:
    var = "oi mais olá "
    var.isalnum -> False
    ***Pois tem espaços em branco.

    isalpha -> Valores alfabéticos.
    isalpha: 'a-z', 'A-Z'

    isdigit -> Apenas valores que possuem os digitos 0-9 no número.

    isdecimal -> Busca por números decimais, ou seja, de base 10.

    isnumeric -> Neste método é verificado os valores númericos que podem ser interiros, subscrito, superbscrito e unicode(EX: \u00BC).


Valores que eu não vou receber por input do usuário -> Booleano, lista, tupla, dicionário
"""
