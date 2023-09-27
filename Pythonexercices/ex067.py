# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.#

while True:
    num = int(input('Quer ver a tabuada de que valor? '))
    print('-' * 35)
    if num < 0:
        break
    for n in range(1, 11):
        prod = n * num
        print(f'{num} x {n:2} = {prod}')
    print('-' * 35)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
