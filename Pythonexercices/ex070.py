# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = contprodut = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if preco > 1000:
        contprodut += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    if perg == 'N':
        break
print('------FIM DO PROGRAMA------')
print(f'A) O total gasto foi de R${total}.')
print(f'B) {contprodut} produto(s) custaram mais de R$1000,00.')
print(f'C) O produto mais barato foi {barato} e custa R${menor:.2f}')
