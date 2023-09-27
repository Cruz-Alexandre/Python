# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
# Desafio 28: Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.#

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0 #variável para poder contar quantas tentativas foram necessárias
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1 # mais um palpite
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tenta mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))

