from models.comparison_result import ResultadoComparacao


class Comparador:

    def comparar(self, jogador1, jogador2):

        pontos_j1 = 0
        pontos_j2 = 0
        detalhes = []

        metricas = [
            ("Jogos", jogador1.jogos, jogador2.jogos),
            ("Gols", jogador1.gols, jogador2.gols),
            ("Assistências", jogador1.assistencias, jogador2.assistencias),
            ("Minutos", jogador1.minutos, jogador2.minutos),
            ("Nota Média", jogador1.nota_media, jogador2.nota_media)
        ]

        for metrica, valor_j1, valor_j2 in metricas:
            vencedor = None

            if valor_j1 > valor_j2:
                pontos_j1 += 1
                vencedor = jogador1
            elif valor_j2 > valor_j1:
                pontos_j2 += 1
                vencedor = jogador2

            detalhes.append({
                "metrica": metrica,
                "valor_j1": self._formatar_valor(valor_j1),
                "valor_j2": self._formatar_valor(valor_j2),
                "vencedor": vencedor
            })

        return ResultadoComparacao(
            jogador1,
            jogador2,
            detalhes,
            pontos_j1,
            pontos_j2
        )

    @staticmethod
    def _formatar_valor(valor):
        if isinstance(valor, float):
            return f"{valor:.2f}"

        return valor
