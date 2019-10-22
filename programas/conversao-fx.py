tabela = {
    'A+': 'Nota é 10.0',
    'A': 'Nota entre 9.5 e 10',
    'A-': 'Nota entre 9.0 e 9.5',
    'B+': 'Nota entre 8.5 e 9.0',
    'B': 'Nota entre 8.0 e 8.5',
    'B-': 'Nota entre 7.5 e 8.0',
    'C+': 'Nota entre 7.0 e 7.5',
    'C': 'Nota entre 6.5 e 7.0',
    'C-': 'Nota entre 6.0 e 6.5',
    'D+': 'Nota entre 5.5 e 6.0',
    'D': 'Nota entre 5.0 e 5.5',
    'D-': 'Nota entre 4.5 e 5.0',
    'F+': 'Nota entre 4.0 e 4.5',
    'F': 'Nota entre 3.5 e 4.0',
    'F-': 'Nota menor que 3.5'
}

nota = input('A nota para conversao: ')
print(tabela[nota])
