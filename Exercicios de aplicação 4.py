class Estacionamento:
    def __init__(self):
        self.pilha = []  # Inicializa uma pilha vazia para armazenar as placas dos carros

    def adicionar_carro(self, placa):
        self.pilha.append(placa)  # Adiciona a placa na pilha

    def verificar_carro(self, placa):
        if placa in self.pilha:
            # Encontrar o índice da placa
            index = self.pilha.index(placa)
            # Carros que precisam ser retirados para o carro em questão sair
            sequencia_retirada = self.pilha[index::-1]  # Retorna a sequência até a placa encontrada
            return sequencia_retirada
        else:
            return None  # Retorna None se a placa não estiver na pilha

# Exemplo de uso
estacionamento = Estacionamento()

# Adicionando carros ao estacionamento
estacionamento.adicionar_carro("ABC1234")
estacionamento.adicionar_carro("DEF5678")
estacionamento.adicionar_carro("GHI9101")
estacionamento.adicionar_carro("JKL1122")

# Placa a ser verificada
placa_para_verificar = "DEF5678"
sequencia = estacionamento.verificar_carro(placa_para_verificar)

if sequencia:
    print(f"Para retirar o carro com a placa {placa_para_verificar}, remova na seguinte sequência: {sequencia}")
else:
    print(f"O carro com a placa {placa_para_verificar} não está estacionado.")
