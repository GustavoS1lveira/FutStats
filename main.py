from services.api import APIFootball
from utils.menu import mostrar_menu
from services.comparator import Comparador
from services.stats import Estatisticas
from services.player_service import ServicoJogador

api = APIFootball()
estatisticas = Estatisticas(api)
servico_jogador = ServicoJogador(api, estatisticas)
comparador = Comparador()


def exibir_entidade(entidade):
    entidade.mostrar_dados()


def main():
    while True:

        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            print("\n===== COMPARAR JOGADORES =====")

            nome1 = input("\nDigite o primeiro jogador: ")
            jogador1 = servico_jogador.selecionar_jogador(nome1)

            if jogador1 is None:
                continue

            nome2 = input("\nDigite o segundo jogador: ")
            jogador2 = servico_jogador.selecionar_jogador(nome2)

            if jogador2 is None:
                continue

            resultado = comparador.comparar(jogador1, jogador2)
            exibir_entidade(resultado)

        elif opcao == "2":

            nome = input("\nDigite o nome do jogador: ")

            jogador = servico_jogador.selecionar_jogador(nome)

            if jogador:
                exibir_entidade(jogador)

        elif opcao == "3":

            print("Saindo do sistema...")
            break

        else:

            print("Opção inválida.")


if __name__ == "__main__":
    main()