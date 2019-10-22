#!/usr/bin/env python

import math

numeros = [int(n) for n in input('Digite uma lista de números: ').split()]
maior = numeros[0]
menor = numeros[0]
media = 0.0
desvio_padrao = 0.0

for n in numeros[1::]:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    media = media + n

media = media / len(numeros)

for n in numeros:
    desvio_padrao = desvio_padrao + math.pow(n - media, 2)

desvio_padrao = math.sqrt(desvio_padrao / len(numeros))

print('Números:', numeros)
print('Maior:', maior)
print('Menor:', menor)
print('Média:', media)
print('Desvio padrão:', desvio_padrao)