def TPilha(vetor):
    pilha = []  # Inicializa uma pilha vazia

    for numero in vetor:
        if numero % 2 == 0:  # Se o número é par
            pilha.append(numero)  # Insere na pilha
        else:  # Se o número é ímpar
            if pilha:  # Verifica se a pilha não está vazia
                pilha.pop()  # Remove o elemento do topo da pilha

    # Esvaziando a pilha e imprimindo os elementos
    while pilha:
        print(pilha.pop())  # Imprime e remove o elemento do topo da pilha

# Exemplo de uso
vetor = [10, 3, 4, 5, 6, 7, 2, 9, 8, 1, 12, 13, 14, 15, 16]
TPilha(vetor)


