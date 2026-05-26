from models.entity import Entidade

class Transferencia(Entidade):

    def __init__(self, jogador, time_origem, time_destino):

        self.jogador = jogador
        self.time_origem = time_origem
        self.time_destino = time_destino

    def mostrar_dados(self):

        print("\n===== TRANSFERÊNCIA =====")

        print(f"Jogador: {self.jogador}")
        print(f"Origem: {self.time_origem}")
        print(f"Destino: {self.time_destino}")