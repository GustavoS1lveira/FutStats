import requests


class APIFootball:

    def buscar_jogador(self, nome_jogador):

        url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={nome_jogador}"

        response = requests.get(url)

        return response.json()

    def buscar_time(self, nome_time):

        url = f"https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t={nome_time}"

        response = requests.get(url)

        return response.json()