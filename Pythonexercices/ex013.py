# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.#

sal = float(input('Qual é o seu salário?R$'))
aum = sal * 15/100
sal_final = sal + aum
print('O seu salário original era de R${:.2f} e após o aumento de 15% foi para R${:.2f}.'.format(sal, sal_final))
