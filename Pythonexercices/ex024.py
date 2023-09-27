# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'.#

cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[0:5].upper() == 'SANTO')


# A solução desse comando foi jogar tudo para maiusculo (tanto upper quanto o nome santo) para que cobrisse todas as opções que o usuario possa colocar.