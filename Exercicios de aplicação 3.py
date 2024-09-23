def pilhas_sao_iguais(pilha1, pilha2):
    # Verifica se as duas pilhas têm o mesmo tamanho
    if len(pilha1) != len(pilha2):
        return False  # Retorna False se os tamanhos forem diferentes

    # Compara os elementos um a um
    for elemento1, elemento2 in zip(pilha1, pilha2):
        if elemento1 != elemento2:
            return False  # Retorna False se encontrar um elemento diferente

    return True  # Retorna True se todas as comparações forem iguais

# Exemplo de uso
pilha1 = [1, 2, 3, 4]
pilha2 = [1, 2, 3, 4]
pilha3 = [4, 3, 2, 1]

print(pilhas_sao_iguais(pilha1, pilha2))  # Saída: True
print(pilhas_sao_iguais(pilha1, pilha3))  # Saída: False
