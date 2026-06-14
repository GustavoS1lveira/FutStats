from models.user import Pessoa
from models.entity import Entidade


class Jogador(Pessoa, Entidade):

    def __init__(
        self,
        nome,
        nacionalidade,
        posicao,
        idade=None,
        altura=None,
        peso=None,
        jogos=0,
        gols=0,
        assistencias=0,
        minutos=0,
        nota_media=0
    ):

        super().__init__(nome, nacionalidade)

        self.posicao = posicao
        self.idade = idade
        self.altura = altura
        self.peso = peso

        self.jogos = jogos
        self.gols = gols
        self.assistencias = assistencias
        self.minutos = minutos
        self.nota_media = nota_media

    def mostrar_dados(self):

        print("\n===== JOGADOR =====")

        print(f"Nome: {self.nome}")
        print(f"Nacionalidade: {self.nacionalidade}")
        print(f"Posição: {self.posicao}")
        print(f"Idade: {self.idade}")

        if self.altura:
            print(f"Altura: {self.altura} cm")

        if self.peso:
            print(f"Peso: {self.peso} kg")

        print(f"Jogos: {self.jogos}")
        print(f"Gols: {self.gols}")
        print(f"Assistências: {self.assistencias}")
        print(f"Minutos: {self.minutos}")

        if self.nota_media:
            print(f"Nota Média: {self.nota_media:.2f}")