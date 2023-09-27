# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

conthomem = contpessoas = contmulher = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        print('-' * 20)
    if idade > 18:
        contpessoas += 1
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F' and idade < 20:
        contmulher += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'A) Foram cadastradas {contpessoas} pessoas com mais de 18 anos.')
print(f'B) Foram cadastrados {conthomem} homens.')
print(f'C) Foram cadastradas {contmulher} mulheres com menos de 20 anos.')
