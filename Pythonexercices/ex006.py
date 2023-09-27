# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.#

n = int(input('Digite um número:'))
print('O dobro de {} vale {}'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raíz quadrada de {} é igual e {:.3f}.'.format(n, (n*3), n, (n**(1/2))))
