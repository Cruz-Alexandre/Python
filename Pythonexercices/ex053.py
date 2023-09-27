# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex. apos a sopa / a sacada da casa / a torre da derrota / o lobo ama o bolo / anotaram a data da maratona.#

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # Aqui separa a frase em bloco, para virar uma lista.#
junto = ''.join(palavras) # Aqui juntou as palavras da frase, excluindo os espaços.#
inverso = ''
for letra in range(len(junto) - 1, -1, -1): #Aqui foi da última letra (len) de junto, até a primeira letra (-1), voltando uma letra (-1).
    inverso += junto[letra] #Aqui desenvolve a variavel inverso, que vai receber a variavel junto invertida pela função FOR.
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')
