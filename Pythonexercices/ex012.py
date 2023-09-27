# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.#

prod = float(input('Qual é o preço do produto? R$'))
desc = prod * 5 / 100
final = prod - desc
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar no final R${:.2f}.'.format(prod, final))
