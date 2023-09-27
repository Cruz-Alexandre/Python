# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.#

valor = float(input('Valor do imóvel: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento: '))
prestacao = valor / (tempo * 12)
regra = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a sua prestação mensal será de R${:.2f}.'.format(valor, tempo, prestacao))
if prestacao < regra:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
