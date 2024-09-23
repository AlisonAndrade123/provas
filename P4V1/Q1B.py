def calculo(n1, n2):
    resultado = (n1**3) / (n2**(1/3))  # Divide n1 elevado ao cubo pela raiz cúbica de n2
    return resultado

n2 = 10   
print(n2)  # Imprime o valor de n2

n1 = 3 
n2 = 27 
print(calculo(n1, n2))  # Chama a função calculo com n1=3 e n2=27
print(n2)  # Imprime o valor de n2 (que agora é 27)
