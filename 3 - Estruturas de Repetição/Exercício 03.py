"""
3 - Faça um programa que leia e valide as seguintes informações:
        a. Nome: maior que 3 caracteres;
        b. Idade: entre 0 e 150;
        c. Salário: maior que zero;
        d. Sexo: 'f' ou 'm';
        e. Estado Civil: 's', 'c', 'v', 'd';
"""


nome = input("Nome: ")
while(len(nome) < 3):
    nome = input("Nome: ")


idade = input("Idade: ")
erro = True
while(erro):
    try:
        idade = int(idade)
        erro = False
        if idade < 0 or idade > 150:
            idade = input("Idade: ")
            erro = True
            
    except:
        erro = True
        idade = input("Idade: ")


salario = input("Salário: ")
erro = True
while(erro):
    try:
        salario = float(salario)
        erro = False
        if salario < 0:
            erro = True
            salario = input("Salário: ")
            
    except:
        erro = True
        salario = input("Salário: ")



sexo = input("Sexo[f ou m]: ")
while(sexo not in ["f", "m"]):
    sexo = input("Sexo[f ou m]: ")

estado_civil = input("Estado Civil[s, c, v, d]: ")

while(estado_civil not in ["s", "c", "v", "d"]):
    estado_civil = input("Estado Civil[s, c, v, d]: ")

