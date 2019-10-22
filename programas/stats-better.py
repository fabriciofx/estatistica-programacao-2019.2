#!/usr/bin/env python

import math

numeros = [int(n) for n in input('Digite uma lista de números: ').split()]
numeros.sort()
maior = numeros[-1]
menor = numeros[0]
media = sum(numeros) / len(numeros)
desvio_padrao = math.sqrt(sum([math.pow(n - media, 2) for n in numeros]) / len(numeros))

print('Números:', numeros)
print('Maior:', maior)
print('Menor:', menor)
print('Média:', media)
print('Desvio padrão:', desvio_padrao)