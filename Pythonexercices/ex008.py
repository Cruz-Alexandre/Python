# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.#
# Durante a aula pediu para acrescentar toda a escala.#

medida = float(input('Uma distância em metros:'))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a: \n{}km \n{}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))


