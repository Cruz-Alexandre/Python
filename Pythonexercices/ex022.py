# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -O nome com todas as letras maiusculas.
# -O nome com todas as letras minusculas.
# -Quantas letras ao todo sem considerar espaços.
# -Quantas letras tem o primeiro nome.

nome = str(input('Digite o nome completo de uma pessoa: ')).strip()
print('Analisando o nome...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
dividido = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0], len(dividido[0])))
