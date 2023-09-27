# Faça um programa que leia a largura e a altura de uma parede em metros, e calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.#

l = float(input('Qual é a largura da parede em metros?'))
a = float(input('Qual é a altura da parede em metros?'))
area = l * a
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, a, area))
print('Para pintar essa parede, você precisará de {} litros de tinta.'.format(area/2))
