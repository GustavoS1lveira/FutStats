from dotenv import load_dotenv
import requests
import os

load_dotenv()


class APIFootball:

    def __init__(self):

        self._api_key = os.getenv("API_FOOTBALL_KEY")

        self._headers = {
            "x-apisports-key": self._api_key
        }

    @property
    def headers(self):
        return self._headers

    def buscar_jogador(self, nome_jogador):

        url = f"https://v3.football.api-sports.io/players/profiles?search={nome_jogador}"

        response = requests.get(
            url,
            headers=self.headers
        )

        return response.json()

    def buscar_estatisticas(self, player_id, season=2020):

        url = (
            f"https://v3.football.api-sports.io/players"
            f"?id={player_id}&season={season}"
        )

        response = requests.get(
            url,
            headers=self.headers
        )

        return response.json()

    def buscar_temporadas_jogador(self, player_id):

        url = (
            f"https://v3.football.api-sports.io/players/seasons"
            f"?player={player_id}"
        )

        response = requests.get(
            url,
            headers=self.headers
        )

        return response.json()