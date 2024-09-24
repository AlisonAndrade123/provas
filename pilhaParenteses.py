def verificar_balanceamento(seq):
    pilha = []
    for char in seq:
        if char == '(':
            pilha.append(char)  # Adiciona parêntese de abertura à pilha
        elif char == ')':
            if not pilha:  # Se a pilha estiver vazia, os parênteses estão desequilibrados
                return False
            pilha.pop()  # Remove o último parêntese de abertura da pilha
    return len(pilha) == 0  # Se a pilha estiver vazia, os parênteses estão balanceados

# Entrada simples do usuário
entrada = input("Digite uma sequência de parênteses: ")
resultado = verificar_balanceamento(entrada)
print(f"{entrada} → {resultado}")
