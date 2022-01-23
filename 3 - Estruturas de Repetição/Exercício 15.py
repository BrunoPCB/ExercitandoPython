"""
15 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
     Faça um programa capaz de gerar a série até o n−ésimo termo.


Ref: https://www.todamateria.com.br/sequencia-de-fibonacci/

Fn = Fn - 1 + Fn - 2

"""


n = input("Infomre o n-ésimo número da serie de Fibonacci: ")
a = 1
b = 0

try:
    n = int(n)
    for i in range(n):
        c = b + a
        a = b
        b = c
        print(c)
        
        

except:
    print("O valor infomado não condiz com o tipo de dado desejado.")