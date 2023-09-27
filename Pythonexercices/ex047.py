# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.#

for num in range(1, 51):
      resto = num % 2
      if resto == 0:
            print(num, end=' ')
print('Acabou!')

for n in range(2, 51, 2):
      print(n, end=' ')
print('Acabou!')

# nesta segunda solução ocupou menos espaço/esforço  na hora de calcular.