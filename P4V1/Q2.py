def triangular(n):
    i = 1
    while i * (i + 1) * (i + 2) <= n:
        if i * (i + 1) * (i + 2) == n:
            return f'É TRIANGULAR'
        i += 1
    return f'NÃO É TRIANGULAR'

num = int(input())
while num != 0:
    print(triangular(num))
    num = int(input())