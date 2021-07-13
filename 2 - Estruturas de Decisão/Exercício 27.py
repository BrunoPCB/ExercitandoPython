"""
27 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                              Até 5 Kg           Acima de 5 Kg
        File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
        Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
        Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

        Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
        de carne da promoção, porém não há limites para a quantidade de carne por cliente.

        Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5%
        sobre o total da compra.

        Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário
        e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne,
        preço total, tipo de pagamento, valor do desconto e valor a pagar.

"""

tipos_carnes = {1: "File Duplo",
                2: "Alcatra",
                3: "Picanha"}

print(f"Escolha uma das carnes:\n"
      f"(1) Filé Duplo\n"
      f"(2) Alcatra\n"
      f"(3) Picanha\n")
tipo_carne = int(input("Resposta: "))

quantidade = float(input("Informe a quantidade de carne(Kg): "))

preco_file, preco_alcatra, preco_picanha, preco, desconto = 0, 0, 0, 0, 0

print("Informe o método de compra:\n"
      "(1) Cartão Tabajara\n"
      "(2) Dinheiro\n")
metodo_compra = int(input("Método de compra desejado: "))

if quantidade <= 5:
    if tipos_carnes[1]:
        preco_file = quantidade * 4.9
        desconto = 0 if metodo_compra == 2 else (preco_file * 0.05)
        preco = preco_file - desconto
    elif tipos_carnes[2]:
        preco_alcatra = quantidade * 5.9
        desconto = 0 if metodo_compra == 2 else (preco_alcatra * 0.05)
        preco = preco_alcatra - desconto
    elif tipos_carnes[3]:
        preco_picanha = quantidade * 6.9
        desconto = 0 if metodo_compra == 2 else (preco_picanha * 0.05)
        preco = preco_picanha - desconto
else:
    if tipos_carnes[1]:
        preco_file = quantidade * 5.8
        desconto = 0 if metodo_compra == 2 else (preco_file * 0.05)
        preco = preco_file - desconto
    elif tipos_carnes[2]:
        preco_alcatra = quantidade * 6.8
        desconto = 0 if metodo_compra == 2 else (preco_alcatra * 0.05)
        preco = preco_alcatra - desconto
    elif tipos_carnes[3]:
        preco_picanha = quantidade * 7.8
        desconto = 0 if metodo_compra == 2 else (preco_picanha * 0.05)
        preco = preco_picanha - desconto


print(f"- - - - - - Nota Fiscal - - - - - - \n"
      f"Tipo de carne:         {tipos_carnes[tipo_carne]}\n"
      f"Quantidade:            {quantidade}Kg\n"
      f"Tipo de pagamento:     {'Cartão Tabajara' if metodo_compra == 1 else 'Dinheiro'}\n"
      f"Desconto:              R${desconto:.2f}\n"
      f"- - - - - - - - - - - - - - - - - - \n"
      f"Total a pagar:         R${preco:.2f}")
