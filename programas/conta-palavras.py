#!/usr/bin/env python

import sys

arquivo = open(str(sys.argv[1]))
texto = arquivo.read().replace('\n', '')
arquivo.close()

num_palavras = len(texto.split())
num_frases = len(texto.split('.'))

print('Quantidade de palavras:', num_palavras)
print('Quantidade de frases:', num_frases)
