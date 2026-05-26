from models.user import Pessoa
from models.entity import Entidade

class Jogador(Pessoa, Entidade):

    def __init__(self, nome, nacionalidade, time, posicao):

        super().__init__(nome, nacionalidade)

        self.time = time
        self.posicao = posicao

    def mostrar_dados(self):

        print("\n===== JOGADOR =====")

        print(f"Nome: {self.nome}")
        print(f"Nacionalidade: {self.nacionalidade}")
        print(f"Time: {self.time}")
        print(f"Posição: {self.posicao}")