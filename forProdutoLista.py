numeros = [2, 3, 4, 5]  # Lista de números
produto = 1  # Inicializamos o produto como 1 (elemento neutro da multiplicação)

# Iteramos sobre a lista e multiplicamos cada número ao valor atual de 'produto'
for num in numeros:
    produto *= num

print(produto)  # Saída: 120
