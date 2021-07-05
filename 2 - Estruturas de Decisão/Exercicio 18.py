"""
18 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
     dezenas e unidades do mesmo.
        Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
        326 = 3 centenas, 2 dezenas e 6 unidades
        12 = 1 dezena e 2 unidades Testar com:
        326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

numero = int(input("Informe um número menor que 1000: "))

if numero < 1000:
      unidade = (numero // 1 % 10)
      dezenas = (numero // 10 % 10)
      centenas = (numero // 100 % 10)

      unidade = str(unidade) + " unidade" if unidade == 1 else str(unidade) + " unidades"
      dezenas = str(dezenas) + " dezena" if dezenas == 1 else str(dezenas) + " dezenas"
      centenas = str(centenas) + " centena" if centenas == 1 else str(centenas) + " centenas"

      print(f"Número: {numero}\n"
            f"Centena(s): {centenas}\n"
            f"Dezena(s): {dezenas}\n"
            f"Unidade(s): {unidade}")
