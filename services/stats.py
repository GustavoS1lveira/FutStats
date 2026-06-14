class Estatisticas:

    @staticmethod
    def calcular(api, player_id):

        temporadas = api.buscar_temporadas_jogador(player_id)

        jogos = 0
        gols = 0
        assistencias = 0
        minutos = 0

        soma_notas = 0
        qtd_notas = 0

        print("\nCalculando estatísticas disponiveis do jogador...")

        for temporada in temporadas["response"]:

            if temporada < 2020:
                continue

            try:

                estatisticas = api.buscar_estatisticas(
                    player_id,
                    temporada
                )

                if estatisticas["results"] == 0:
                    continue

                stats = estatisticas["response"][0]["statistics"]

                for competicao in stats:

                    jogos += competicao["games"]["appearences"] or 0
                    gols += competicao["goals"]["total"] or 0
                    assistencias += competicao["goals"]["assists"] or 0
                    minutos += competicao["games"]["minutes"] or 0

                    nota = competicao["games"]["rating"]

                    if nota is not None:
                        soma_notas += float(nota)
                        qtd_notas += 1

            except Exception:
                continue

        nota_media = 0

        if qtd_notas > 0:
            nota_media = soma_notas / qtd_notas

        return {
            "jogos": jogos,
            "gols": gols,
            "assistencias": assistencias,
            "minutos": minutos,
            "nota_media": nota_media
        }