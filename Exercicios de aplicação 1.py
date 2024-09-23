def maior_elemento(pilha):
    # Verifica se a pilha está vazia
    if not pilha:
        return None  # Retorna None se a pilha estiver vazia

    maior = pilha[0]  # Inicializa o maior elemento com o primeiro da pilha

    for elemento in pilha:
        if elemento > maior:
            maior = elemento  # Atualiza o maior se encontrar um elemento maior

    return maior  # Retorna o maior elemento encontrado

# Exemplo de uso
pilha = [3, 5, 2, 9, 1]
print(maior_elemento(pilha))  # Saída: 9
