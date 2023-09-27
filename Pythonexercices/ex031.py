# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0.5 por km para viagens de até 200km e R$0,45 para viagens mais longe.#

distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distância))
if distância <= 200:
    preço = distância * 0.5
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(preço))
