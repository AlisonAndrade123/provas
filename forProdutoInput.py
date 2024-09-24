
# Inicializamos o produto como 1 (elemento neutro da multiplicação)
produto = 1

# Definimos quantos números serão multiplicados
quantidade = int(input("Quantos números você quer multiplicar? "))

# Usamos um loop para obter os números e calcular o produto
for i in range(quantidade):
    numero = int(input(f"Digite o número: "))
    produto *= numero

print(f"O produto dos números é: {produto}")
