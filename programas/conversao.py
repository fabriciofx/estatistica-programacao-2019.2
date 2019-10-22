tipo = 'inicio'
while(tipo == 'inicio' or tipo == 'ab' or tipo == 'ba'):
    tipo = input('Qual é o tipo de conversão? ')
    if tipo == 'ab':
        print('Convertendo de Americano para Brasileiro')
        nota_ab = input('A nota para conversao: ')
        if nota_ab == 'A+':
            print('Nota é 10.0')
        elif nota_ab == 'A':
            print('Nota entre 9.5 e 10')
        elif nota_ab == 'A-':
            print('Nota entre 9.0 e 9.5')
        elif nota_ab == 'B+':
            print('Nota entre 8.5 e 9.0')
        elif nota_ab == 'B':
            print('Nota entre 8.0 e 8.5')
        elif nota_ab == 'B-':
            print('Nota entre 7.5 e 8.0')
        elif nota_ab == 'C+':
            print('Nota entre 7.0 e 7.5')
        elif nota_ab == 'C':
            print('Nota entre 6.5 e 7.0')
        elif nota_ab == 'C-':
            print('Nota entre 6.0 e 6.5')
        elif nota_ab == 'D+':
            print('Nota entre 5.5 e 6.0')
        elif nota_ab == 'D':
            print('Nota entre 5.0 e 5.5')
        elif nota_ab == 'D-':
            print('Nota entre 4.5 e 5.0')
        elif nota_ab == 'F+':
            print('Nota entre 4.0 e 4.5')
        elif nota_ab == 'F':
            print('Nota entre 3.5 e 4.0')
        elif nota_ab == 'F-':
            print('Nota menor que 3.5')
        else:
            print('Nota digitada inválida')
    elif tipo == 'ba':
        print('Convertendo de Brasileiro para Americano')
        nota_ba = float(input('A nota para conversao: '))
        if nota_ba >= 10:
            print("Sua nota é A+")
        elif nota_ba >= 9.5:
            print("Sua nota é A")
        elif nota_ba >= 9:
            print("Sua nota é A-")
        elif nota_ba >= 8.5:
            print("Sua nota é B+")
        elif nota_ba >= 8:
            print("Sua nota é B")
        elif nota_ba >= 7.5:
            print("Sua nota é B-")
        elif nota_ba >= 7:
            print("Sua nota é C+")
        elif nota_ba >= 6.5:
            print("Sua nota é C")
        elif nota_ba >= 6:
            print("Sua nota é C-")
        elif nota_ba >= 5.5:
            print("Sua nota é D+")
        elif nota_ba >= 5:
            print("Sua nota é D")
        elif nota_ba >= 4.5:
            print("Sua nota é D-")
        elif nota_ba >= 4:
            print("Sua nota é F+")
        elif nota_ba >= 3.5:
            print("Sua nota é F")
        else:
            print("Sua nota é F-")
    else:
        print('ESCREVA NO PADRAO CORRETO!')
