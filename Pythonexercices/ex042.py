# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais. Isósceles: dois lados iguais. Escaleno: Todos os lados diferentes.
# ex035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.#

print('\033[33m-*-' * 10)
print('Analisador de triângulos')
print('-*-' * 10, '\033[m')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os valores de segmentos acima formam um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isósceles.')
    else:
        print('Escaleno.')
else:
    print('Os valores de segmentos acima \033[1;31mNÃO\033[m formam um triângulo.')
