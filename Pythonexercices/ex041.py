# A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM, até 14 anos: INFANTIL, até 19 anos: JUNIOR, até 25 anos: SENIOR, acima: MASTER.

from datetime import date
nascimento = int(input('Ano de nascimento: '))
ano = date.today().year
dif = ano - nascimento
print('O atleta que nasceu no ano de {} possui em {}, {} anos.'.format(nascimento, ano, dif))
if dif <= 9:
    print('O atleta pertence a categoria MIRIM.')
elif 9 < dif <= 14:
    print('O atleta pertence a categoria INFANTIL.')
elif 14 < dif <= 19:
    print('O atleta pertence a categoria JUNIOR')
elif 19 < dif <= 25:
    print('O atleta pertence a categoria SENIOR.')
elif dif >25:
    print('O atleta pertence a categoria MASTER')
