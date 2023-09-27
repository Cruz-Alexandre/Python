# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.#

km = float(input('Quantos km foram percorridos: '))
d = int(input('Quantos dias? '))
preco = (60 * d) + (0.15 * km)
print('Você vai pagar R${:.2f} pelo aluguel do carro.'.format(preco))
