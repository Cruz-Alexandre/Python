# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar. - Se é a hora de se alistar. - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.#

from datetime import date
print('''\033[4mEscolha uma das opções abaixo\033[m: 
[ 1 ] Masculino
[ 2 ] Feminino''')
sexo = int(input('Qual a sua opção? '))
if sexo == 2:
    print('Pessoas do sexo feminino \033[1;31mNÃO\033[m precisam se alistar!')
else:
    print('Como você é do sexo masculino, responda:')
    nascimento = int(input('Ano de nascimento: '))
    ano = date.today().year
    idade = ano - nascimento
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano))
    if ano - nascimento < 18:
        print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(nascimento + 18))
    elif ano - nascimento == 18:
        print('Você precisa se alistar ao serviço militar imediatamente.')
    elif ano - nascimento > 18:
        print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(ano - (idade - 18)))
