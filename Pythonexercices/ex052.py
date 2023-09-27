# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.#

num = int(input('Digite um número: '))
tot = 0 # criou essa variavel de contador com nome tot para saber o número de divisiveis
for c in range(1, num + 1):
    if num % c == 0:     # se o número escolhido tiver o resto da divisão com o contador c igual a zero. Isso significa que ele é divisivel por ele mesmo.
        print('\033[33m', end=' ')
        tot += 1 # tot = tot + 1. Aqui é onde conta quantas vezes o num atende a condição acima de if
    else:
        print('\033[31m', end=' ')  # toda essa parte do if else com \033 é para fazer uma graça para colocar uma cor nos números.
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2: # Para ser primo, só pode ser divisivel 2 vezes, por 1 e por ele mesmo.
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')
