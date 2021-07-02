"""
14 - Faça um Programa que peça os 3 lados de um triângulo.
     O programa deverá informar se os valores podem ser um triângulo.
     Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
     Dicas:
        Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
        Triângulo Equilátero: três lados iguais;
        Triângulo Isósceles: quaisquer dois lados iguais;
        Triângulo Escaleno: três lados diferentes;
"""

a = int(input("Informe o lado a: "))
b = int(input("Informe o lado b: "))
c = int(input("Informe o lado c: "))


if (b - c) < a < b + c:
    triangulo_verdadeiro = True
elif (a - c) < b < a + c:
    triangulo_verdadeiro = True
elif (a - b) < c < a + b:
    triangulo_verdadeiro = True
else:
    triangulo_verdadeiro = False
    print(f"Este não é um triângulo")

if triangulo_verdadeiro:
    # Triangulo Equilátero
    if a == b == c:
        triangulo_equilitario = True
        print(f"Com estas medidas, você tem um triângulo Equilátero")

    # Triangulo Isósceles
    if a == b or b == c or a == c:
        triangulo_isosceles = True
        print(f"Com estas medidas, você tem um triângulo Isósceles")

    # Triangulo Escaleno
    if a != b and b != c and a != c:
        triangulo_escaleno = True
        print(f"Com estas medidas, você tem um triângulo Escaleno")

