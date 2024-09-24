def soma(n):
    if len(n) == 0:
        return 0
    else:
        return int(n[-1]) + soma(n[:-1])

n = str(input('Digite um número: '))
while n != '0' and n != '':
    print(soma(n))
    n = str(input('Digite um número: '))