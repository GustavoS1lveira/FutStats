from models.entity import Entidade

class Time(Entidade):
    def __init__(self, nome, liga, estadio):
        self.nome = nome
        self.liga = liga
        self.estadio = estadio

    def mostrar_dados(self):
        print("\n===== TIME =====")
        print(f"Nome: {self.nome}")
        print(f"Liga: {self.liga}")
        print(f"Estádio: {self.estadio}")