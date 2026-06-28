class Pessoa:

    def __init__(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

    @property
    def nome(self):
        return self._nome

    @property
    def nacionalidade(self):
        return self._nacionalidade

    def mostrar_pessoa(self):
        print(f"Nome: {self.nome}")
        print(f"Nacionalidade: {self.nacionalidade}")