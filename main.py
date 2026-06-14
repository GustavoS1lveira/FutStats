from services.api import APIFootball
from models.player import Jogador
from utils.menu import mostrar_menu
from services.comparator import Comparador
from services.stats import Estatisticas

api = APIFootball()


def selecionar_jogador(nome_busca):

    dados = api.buscar_jogador(nome_busca)

    if dados["results"] == 0:
        print("Jogador não encontrado.")
        return None

    jogadores = dados["response"]

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

    try:

        escolha = int(input("\nEscolha um jogador: ")) - 1

        if not (0 <= escolha < len(jogadores[:5])):
            print("Escolha inválida.")
            return None

        jogador_api = jogadores[escolha]["player"]

        player_id = jogador_api.get("id")

        dados_estatisticas = Estatisticas.calcular(
            api,
            player_id
        )

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

while True:

    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print("\n===== COMPARAR JOGADORES =====")

        nome1 = input("\nDigite o primeiro jogador: ")
        jogador1 = selecionar_jogador(nome1)

        if jogador1 is None:
            continue

        nome2 = input("\nDigite o segundo jogador: ")
        jogador2 = selecionar_jogador(nome2)

        if jogador2 is None:
            continue

        Comparador.comparar(jogador1, jogador2)

    elif opcao == "2":

        nome = input("\nDigite o nome do jogador: ")

        jogador = selecionar_jogador(nome)

        if jogador:
            jogador.mostrar_dados()

    elif opcao == "3":

        print("Saindo do sistema...")
        break

    else:

        print("Opção inválida.")