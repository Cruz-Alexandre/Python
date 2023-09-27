# Crie um programa que leia quanto dinheiro que uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1.00 = R$ 3.27.#

r = float(input('Quanto dinheiro você possui na carteira? R$'))
d = r / 3.27
print('Você possui R${:.2f} e você pode comprar US${:.2f}.'.format(r, d))
