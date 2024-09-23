def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    anterior = 1
    corrente = 1
    for i in range(n-2):
        proximo = anterior + corrente
        anterior = corrente
        corrente = proximo
    return corrente

num = int(input())
while num != 0:
    print(fibonacci(num))
    num = int(input())