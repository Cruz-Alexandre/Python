# Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR. #
# ex009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.#

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
