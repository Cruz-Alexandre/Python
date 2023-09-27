# Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e que se encontram no intervalo de 1 a 500.#

soma = 0 # conceito de acumulador #
cont = 0 # conceito de contador #
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # pode sempre colocar cont += 1 (cont recebe ele mesmo + 1) #
        soma = soma + c # pode sempre colocar soma += c (soma recebe ele mesmo + c) #
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
