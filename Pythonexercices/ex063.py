# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8#

print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 25)
print('{} -> {}'.format(t1, t2), end='')
cont = 3 # o contador começa em 3 pq já mostrou o primeiro e o segundo termo
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' -> FIM')
print('~' * 25)
