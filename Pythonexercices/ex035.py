# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.#

print('\033[33m-=-' * 15)
print('Analisador de Triângulos')
print('-=-' * 15, '\033[m')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo.')
else:
    print('Os seguimentos acima \033[1;31mNÃO\033[m podem formar um triângulo.')
