# Função que aceita qualquer quantidade de números e calcula o produto
def produto(*numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

# Chamando a função com números individuais
resultado_produto = produto(2, 3, 4, 5)
print(resultado_produto)  # Saída: 120
