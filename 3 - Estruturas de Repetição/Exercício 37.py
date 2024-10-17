"""
37 - Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o
     mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua
     altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
     Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais
     gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""

clientes = {}
cod_cliente = 0

print('Informe "0" no código do cliente para terminar o cadastro de clientes.')
while True:
    cod_cliente = int(input('Informe seu código de cliente: '))

    if cod_cliente == 0:
        break

    clientes[cod_cliente] = []
    clientes[cod_cliente].append(float(input('Informe seu peso: ')))
    clientes[cod_cliente].append(float(input('Informe seu tamanho: ')))

pesos = []
alturas = []

for cliente in clientes.values():
    pesos.append(cliente[0])
    alturas.append(cliente[1])

    pesos.sort()
    alturas.sort()


resultado = {
    "gordo":pesos[-1],
    "magro":pesos[0],
    "alto":alturas[-1],
    "baixo":alturas[0],
}

print(resultado)