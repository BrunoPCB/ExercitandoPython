"""
2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite 
    a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando
    a pedir as informações.
"""

def checkup(usuario, senha):
    erro = False if usuario != senha else True
    return erro

erro = True

usuario = input("Informe um nome de usuário: ")

senha = input("Informe uma senha: ")

erro = checkup(usuario, senha)

if erro:
    print("Erro no cadastro! Senha deve ser difirente do usuário.")
else:
    print("Cadastro comleto.")


while(erro):

    usuario = input("Informe um nome de usuário: ")

    senha = input("Informe uma senha: ")

    erro = checkup(usuario, senha)

    if erro == False:
        print("Cadastro comleto.")
        break
    else:
        print("Erro no cadastro! Senha deve ser difirente do usuário.")
        erro = True


    
