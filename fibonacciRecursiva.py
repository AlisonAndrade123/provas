def fibonacci(n):
    if n <= 2: 
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
num = int(input())
while num != 0:
    print(fibonacci(num))
    num = int(input())