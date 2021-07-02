"""
15 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
     O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário
     nas seguintes situações:
        Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa
        não deve fazer pedir os demais valores, sendo encerrado;
        Se o delta calculado for negativo, a equação não possui raizes reais.
        Informe ao usuário e encerre o programa;
        Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
        informe-a ao usuário;
        Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
from math import sqrt

# Formula ax + b + c
a = int(input("Informe um valor para a: "))
b = int(input("Informe um valor para b: "))
c = int(input("Informe um valor para c: "))

if a == 0:
    print("Esta equação não é do 2º grau.")

delta = (b ** 2) - 4 * a * c

if delta < 0:
    print("Essa equação não tem raizes reais.")

if delta == 0:
    x1 = -b + sqrt(delta) / 2 * a
    x2 = -b - sqrt(delta) / 2 * a
    print("Delta == 0 --> ", x1, x2)

elif delta > 0:
    x1 = -b + sqrt(delta) / 2 * a
    x2 = -b - sqrt(delta) / 2 * a
    print("Delta > 0 --> ", x1, x2)

