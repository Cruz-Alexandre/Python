# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcue seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de  18.5: Abaixo do peso; entre 18.5 e 25: Peso ideal; 20 até 30: Sobrepeso; 30 até 40: Obesidade; Acima de 40: Obesidade mórbida.#

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está Abaixo do peso.')
elif imc < 25:
    print('Parabéns, você está na faixa de Peso ideal.')
elif imc < 30:
    print('Você está em Sobrepeso')
elif imc < 40:
    print('Você está em Obesidade')
else:
    print('Você está em Obesidade mórbida.')
