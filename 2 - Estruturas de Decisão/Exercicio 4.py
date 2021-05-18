"""
4  - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

consoantes = ['c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
vogais = ['a','e','i','o','u','A','E','I','O','U']

letra = input("Informe uma letra: ")

if letra in consoantes:
    print(f"A letra {letra} é uma CONSOANTE.")
elif letra in vogais:
    print(f"A letra {letra} é uma VOGAL.")
else:
    print(f"'{letra}' não é uma letra.")
