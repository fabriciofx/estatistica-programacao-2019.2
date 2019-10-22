
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)

if __name__ == '__main__':
    num = int(input('Digite um número: '))
    resultado = fatorial(num)
    print('O fatorial de', num, 'é', resultado)
