from abc import ABC, abstractmethod
class Entidade(ABC):

    @abstractmethod
    def mostrar_dados(self):
        pass