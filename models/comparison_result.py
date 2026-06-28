from models.entity import Entidade


class ResultadoComparacao(Entidade):

    def __init__(self, jogador1, jogador2, detalhes, pontos_j1, pontos_j2):
        self._jogador1 = jogador1
        self._jogador2 = jogador2
        self._detalhes = detalhes
        self._pontos_j1 = pontos_j1
        self._pontos_j2 = pontos_j2

    @property
    def jogador1(self):
        return self._jogador1

    @property
    def jogador2(self):
        return self._jogador2

    @property
    def detalhes(self):
        return self._detalhes

    @property
    def pontos_j1(self):
        return self._pontos_j1

    @property
    def pontos_j2(self):
        return self._pontos_j2

    @property
    def vencedor(self):
        if self.pontos_j1 > self.pontos_j2:
            return self.jogador1

        if self.pontos_j2 > self.pontos_j1:
            return self.jogador2

        return None

    def mostrar_dados(self):
        print("\n===== COMPARAÇÃO =====\n")

        for detalhe in self.detalhes:
            print(
                f"{detalhe['metrica']}: "
                f"{detalhe['valor_j1']} x {detalhe['valor_j2']}"
            )

            if detalhe["vencedor"]:
                print(f"Vencedor: {detalhe['vencedor'].nome}")
            else:
                print("Empate")

            print()

        print("==============================")
        print("\nPLACAR FINAL\n")
        print(f"{self.jogador1.nome}: {self.pontos_j1} pontos")
        print(f"{self.jogador2.nome}: {self.pontos_j2} pontos")

        if self.vencedor:
            print(f"\nVENCEDOR: {self.vencedor.nome}")
        else:
            print("\nRESULTADO: EMPATE")
