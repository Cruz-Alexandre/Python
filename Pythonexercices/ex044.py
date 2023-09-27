# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
# - A vista dinheiro/cheque: 10% de desconto. - A vista no cartão: 5% de desconto. - Em até 2x no cartão: preço normal. - 3x ou mais no cartão: 20% de juros.#

print('\033[33m{} CASAS CRUZ {}\033[m'.format('=' * 15, '=' * 15))
print('{:=^40}'.format(' CASAS CRUZ '))
valor = float(input('Preço das compras? R$'))
print('''Formas de Pagamento:
[ 1 ] À vista dinheiro/cheque.
[ 2 ] À vista no cartão.
[ 3 ] 2X no cartão.
[ 4 ] 3x ou mais no cartão.''')
forma = int(input('Escolha uma opção como forma de pagamento: '))
if forma == 1:
    total = valor - (valor * 10 / 100)
elif forma == 2:
    total = valor - (valor * 5 / 100)
elif forma == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif forma == 4:
    total = valor + (valor * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totparc, parcela))
else:
    total = valor
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))
