class Jogador:
    def __init__(self, nome, time, nacionalidade, posicao):
        self.nome = nome
        self.time = time
        self.nacionalidade = nacionalidade
        self.posicao = posicao

    def mostrar_dados(self):
        print("\n===== MERCADO DA BOLA =====")
        print(f"Nome: {self.nome}")
        print(f"Time: {self.time}")
        print(f"Nacionalidade: {self.nacionalidade}")
        print(f"Posição: {self.posicao}")