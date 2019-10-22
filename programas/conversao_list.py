tipo = 'inicio'
notas_americanas = ['F-','F','F+','D-','D','D+','C-','C','C+','B-','B','B+','A-','A','A+']
while(tipo == 'inicio' or tipo == 'ab' or tipo == 'ba'):
    tipo = input('Qual é o tipo de conversão? ')
    if tipo == 'ab':
        print('Convertendo de Americano para Brasileiro')
        nota_ab = input('A nota para conversao: ')
        indice = notas_americanas.index(nota_ab)
        nota_convertida = (indice + 6) / 2
        print(nota_convertida)
    elif tipo == 'ba':
        print('Convertendo de Brasileiro para Americano')
        nota_ba = float(input('A nota para conversao: '))
        indice_nota_convertida = int(2 * (nota_ba - 3))
        if indice_nota_convertida < 0:
            indice_nota_convertida = 0
        print(notas_americanas[indice_nota_convertida])
    else:
        print('ESCREVA NO PADRAO CORRETO!')