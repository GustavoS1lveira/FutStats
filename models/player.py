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

        self._posicao = posicao
        self._idade = idade
        self._altura = altura
        self._peso = peso

        self._jogos = self._valor_positivo(jogos)
        self._gols = self._valor_positivo(gols)
        self._assistencias = self._valor_positivo(assistencias)
        self._minutos = self._valor_positivo(minutos)
        self._nota_media = self._valor_positivo(nota_media)

    @staticmethod
    def _valor_positivo(valor):
        if valor is None:
            return 0

        return max(valor, 0)

    @property
    def posicao(self):
        return self._posicao

    @property
    def idade(self):
        return self._idade

    @property
    def altura(self):
        return self._altura

    @property
    def peso(self):
        return self._peso

    @property
    def jogos(self):
        return self._jogos

    @property
    def gols(self):
        return self._gols

    @property
    def assistencias(self):
        return self._assistencias

    @property
    def minutos(self):
        return self._minutos

    @property
    def nota_media(self):
        return self._nota_media

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