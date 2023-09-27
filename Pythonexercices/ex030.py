# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.#

num = int(input('Me diga um número qualquer: '))
resto = num % 2
if resto == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))
