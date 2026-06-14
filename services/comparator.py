class Comparador:

    @staticmethod
    def comparar(jogador1, jogador2):

        pontos_j1 = 0
        pontos_j2 = 0

        print("\n===== COMPARAÇÃO =====\n")

        print(f"Jogos: {jogador1.jogos} x {jogador2.jogos}")

        if jogador1.jogos > jogador2.jogos:
            pontos_j1 += 1
            print(f"Vencedor: {jogador1.nome}")
        elif jogador2.jogos > jogador1.jogos:
            pontos_j2 += 1
            print(f"Vencedor: {jogador2.nome}")
        else:
            print("Empate")

        print()

        print(f"Gols: {jogador1.gols} x {jogador2.gols}")

        if jogador1.gols > jogador2.gols:
            pontos_j1 += 1
            print(f"Vencedor: {jogador1.nome}")
        elif jogador2.gols > jogador1.gols:
            pontos_j2 += 1
            print(f"Vencedor: {jogador2.nome}")
        else:
            print("Empate")

        print()

        print(
            f"Assistências: "
            f"{jogador1.assistencias} x {jogador2.assistencias}"
        )

        if jogador1.assistencias > jogador2.assistencias:
            pontos_j1 += 1
            print(f"Vencedor: {jogador1.nome}")
        elif jogador2.assistencias > jogador1.assistencias:
            pontos_j2 += 1
            print(f"Vencedor: {jogador2.nome}")
        else:
            print("Empate")

        print()

        print(f"Minutos: {jogador1.minutos} x {jogador2.minutos}")

        if jogador1.minutos > jogador2.minutos:
            pontos_j1 += 1
            print(f"Vencedor: {jogador1.nome}")
        elif jogador2.minutos > jogador1.minutos:
            pontos_j2 += 1
            print(f"Vencedor: {jogador2.nome}")
        else:
            print("Empate")

        print()

        print(
            f"Nota Média: "
            f"{jogador1.nota_media:.2f} x {jogador2.nota_media:.2f}"
        )

        if jogador1.nota_media > jogador2.nota_media:
            pontos_j1 += 1
            print(f"Vencedor: {jogador1.nome}")
        elif jogador2.nota_media > jogador1.nota_media:
            pontos_j2 += 1
            print(f"Vencedor: {jogador2.nome}")
        else:
            print("Empate")

        print("\n==============================")
        print("\nPLACAR FINAL\n")

        print(f"{jogador1.nome}: {pontos_j1} pontos")
        print(f"{jogador2.nome}: {pontos_j2} pontos")

        if pontos_j1 > pontos_j2:
            print(f"\n🏆 VENCEDOR: {jogador1.nome}")
        elif pontos_j2 > pontos_j1:
            print(f"\n🏆 VENCEDOR: {jogador2.nome}")
        else:
            print("\n🏆 RESULTADO: EMPATE")
