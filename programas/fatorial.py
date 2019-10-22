num = int(input('Digite um número: '))
resultado = 1
for i in range(1, num + 1):
    resultado = resultado * i
print('O fatorial de', num, 'é', resultado)
