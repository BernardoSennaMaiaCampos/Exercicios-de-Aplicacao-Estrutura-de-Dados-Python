def imprimir_ordem_inversa(numeros):
    pilha = []  # Cria uma pilha vazia

    # Empilha os números
    for numero in numeros:
        pilha.append(numero)

    # Desempilha e imprime os números na ordem inversa
    while pilha:
        print(pilha.pop())

# Exemplo de uso
n = int(input("Digite a quantidade de números: "))
numeros = []

for _ in range(n):
    numero = float(input("Digite um número real: "))
    numeros.append(numero)

imprimir_ordem_inversa(numeros)
