x = int(input("Digite um número inteiro: "))
quantidade = 0


while quantidade < 20:
    if x > 1:
        e_primo = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                e_primo = False
                break
        if e_primo:
            print(x)
            quantidade += 1
    x += 1
