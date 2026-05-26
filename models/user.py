class Pessoa:

    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def mostrar_pessoa(self):
        print(f"Nome: {self.nome}")
        print(f"Nacionalidade: {self.nacionalidade}")