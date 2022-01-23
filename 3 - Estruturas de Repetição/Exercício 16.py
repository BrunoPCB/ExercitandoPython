"""
16 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.
"""

a = 1
b = 0
c = 0

while(c < 500):
    c = b + a
    a = b
    b = c

    print(c)

print("The End")