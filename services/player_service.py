from models.player import Jogador


class ServicoJogador:

    def __init__(self, api, estatisticas):
        self._api = api
        self._estatisticas = estatisticas

    def selecionar_jogador(self, nome_busca):
        dados = self._api.buscar_jogador(nome_busca)

        if dados["results"] == 0:
            print("Jogador não encontrado.")
            return None

        jogadores = dados["response"]
        self._mostrar_opcoes(jogadores)

        try:
            escolha = int(input("\nEscolha um jogador: ")) - 1

            if not (0 <= escolha < len(jogadores[:5])):
                print("Escolha inválida.")
                return None

            jogador_api = jogadores[escolha]["player"]
            player_id = jogador_api.get("id")
            dados_estatisticas = self._estatisticas.calcular(player_id)

            return Jogador(
                nome=jogador_api.get("name", "Desconhecido"),
                nacionalidade=jogador_api.get("nationality", "Desconhecida"),
                posicao=jogador_api.get("position", "Sem posição"),
                idade=jogador_api.get("age"),
                altura=jogador_api.get("height"),
                peso=jogador_api.get("weight"),
                jogos=dados_estatisticas["jogos"],
                gols=dados_estatisticas["gols"],
                assistencias=dados_estatisticas["assistencias"],
                minutos=dados_estatisticas["minutos"],
                nota_media=dados_estatisticas["nota_media"]
            )

        except ValueError:
            print("Digite um número válido.")
            return None

    @staticmethod
    def _mostrar_opcoes(jogadores):
        print("\nJogadores encontrados:\n")

        for i, item in enumerate(jogadores[:5]):
            jogador_api = item["player"]

            nome = jogador_api.get("name", "Desconhecido")
            posicao = jogador_api.get("position", "Sem posição")
            idade = jogador_api.get("age", "?")
            nacionalidade = jogador_api.get("nationality", "N/A")

            print(
                f"{i + 1} - {nome} | "
                f"{posicao} | "
                f"{idade} anos | "
                f"{nacionalidade}"
            )
