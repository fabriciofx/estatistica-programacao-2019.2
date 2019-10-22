#!/usr/bin/env python

# 0 . Preparação: importa os pacotes sys (para extrair os argumentos de execução
#     do script) e re (expressão regulares)
import sys, re

# 1. Abre o arquivo de texto
arquivo = open(sys.argv[1], encoding = 'utf-8')

# 2. 'Limpa' o conteúdo do arquivo de texto (trocar duas ou mais ocorrências de
#    espaços em branco ou quebra de linha por um único espaço em branco) e
#    armazena em uma variável
texto = re.sub(r'\s+', ' ', arquivo.read())

# 3. Fecha o arquivo (tudo o que é aberto, tem que depois de usado, fechar)
arquivo.close()

# 4. Quebra o conteúdo limpo do arquivo nas ocorrências onde há um espaço em
#    branco, transformando em uma lista de palavras
palavras = texto.split(' ')

# 5. Quebra o conteúdo limpo do arquivo nas ocorrências onde há um ponto (final
#    de frase) transformando em uma lista de frases
frases = texto.split('.')

# 6. Exibe no console a quantidade de elementos que há na lista de palavras
print('Quantidade de palavras:', len(palavras))

# 7. Exibe no console a quantidade de elementos que há na lista de frases
print('Quantidade de frases:', len(frases))
