from services.api import APIFootball
from models.player import Jogador
from models.team import Time
from utils.menu import mostrar_menu


api = APIFootball()

while True:

    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    # =========================
    # BUSCAR JOGADOR
    # =========================
    if opcao == "1":

        nome = input("Digite o nome do jogador: ")

        dados = api.buscar_jogador(nome)

        print(dados)

        if dados["player"] is not None:

            jogadores_filtrados = []

            # Filtra apenas jogadores de futebol
            for player in dados["player"]:

                esporte = player.get("strSport")

                if esporte == "Soccer":

                    jogadores_filtrados.append(player)

            if len(jogadores_filtrados) > 0:

                print("\nJogadores encontrados:\n")

                # Mostra apenas os 5 primeiros
                for i, player in enumerate(jogadores_filtrados[:5]):

                    nome_jogador = player.get("strPlayer", "Desconhecido")
                    time_jogador = player.get("strTeam", "Sem time")

                    print(f"{i + 1} - {nome_jogador} ({time_jogador})")

                escolha = int(input("\nEscolha um jogador: ")) - 1

                # Validação simples
                if 0 <= escolha < len(jogadores_filtrados[:5]):

                    jogador_api = jogadores_filtrados[escolha]

                    jogador = Jogador(

                        jogador_api.get("strPlayer", "Desconhecido"),
                        jogador_api.get("strNationality", "Desconhecida"),
                        jogador_api.get("strTeam", "Sem time"),
                        jogador_api.get("strPosition", "Sem posição")

                    )

                    jogador.mostrar_dados()

                else:
                    print("Escolha inválida.")

            else:
                print("Nenhum jogador correspondente encontrado.")

        else:
            print("Jogador não encontrado.")

    # =========================
    # BUSCAR TIME
    # =========================
    elif opcao == "2":

        nome = input("Digite o nome do time: ")

        dados = api.buscar_time(nome)

        if dados["teams"] is not None:

            times_filtrados = []

            for team in dados["teams"]:

                nome_api = team.get("strTeam", "")

                if nome.lower() in nome_api.lower():

                    times_filtrados.append(team)

            if len(times_filtrados) > 0:

                print("\nTimes encontrados:\n")

                # Mostra apenas os 5 primeiros
                for i, team in enumerate(times_filtrados[:5]):

                    print(f"{i + 1} - {team.get('strTeam', 'Desconhecido')}")

                escolha = int(input("\nEscolha um time: ")) - 1

                # Validação simples
                if 0 <= escolha < len(times_filtrados[:5]):

                    time_api = times_filtrados[escolha]

                    time = Time(

                        time_api.get("strTeam", "Desconhecido"),
                        time_api.get("strLeague", "Liga desconhecida"),
                        time_api.get("strStadium", "Estádio desconhecido")

                    )

                    time.mostrar_dados()

                else:
                    print("Escolha inválida.")

            else:
                print("Nenhum time correspondente encontrado.")

        else:
            print("Time não encontrado.")


    elif opcao == "3":

        print("Saindo do sistema...")
        break

    else:

        print("Opção inválida.")