# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.#

from random import randint
from time import sleep #serve para que crie um suspense após vc escolher um número mais abaixo#
computador = randint(0, 5) # Faz o computador escolher um número#
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador= int(input('Em que número pensei? ')) #jogador tenta adivinhar#
print('PROCESSANDO...')
sleep(3) #aqui você coloca o tempo que quiser#
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))
