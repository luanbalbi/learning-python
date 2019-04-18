def computador_escolhe_jogada(n, m):
    jogada = m
    if m >= n:
        jogada = n
    else:
        while jogada > 1:
            if ((n - jogada) % (m + 1) == 0):
                return jogada
            else:
                jogada = jogada - 1
    return jogada

def usuario_escolhe_jogada(n, m):
    jogada_valida = False
    while not jogada_valida:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada >= 1 and jogada <= m:
            return jogada
        else:
            print("\nOops! Jogada inválida! Tente de novo.\n")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if (n % (m + 1) == 0):
        print("\nVoce começa!\n")
        vez_maquina = False
    else:
        print("\nComputador começa!\n")
        vez_maquina = True

    while n > 0:
        if vez_maquina:
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada

            if jogada > 1:
                print("O computador tirou", jogada, "peças.")
            else:
                print("O computador tirou uma peça.")

            if n > 1:
                print("Agora restam", n, "peças no tabuleiro.\n")
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Fim do jogo! O computador ganhou!\n")
                return True
            vez_maquina = False
        else:
            jogada = usuario_escolhe_jogada(n, m)
            n = n - jogada

            if jogada > 1:
                print("Voce tirou", jogada, "peças.")
            else:
                print("Você tirou uma peça.")

            if n > 1:
                print("Agora restam", n, "peças no tabuleiro.\n")
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Fim do jogo! Você ganhou!\n")
                return False
            vez_maquina = True

def campeonato():
    rodada = 1
    placar_maquina = placar_jogador = 0
    while rodada <=3:
        print("**** Rodada", rodada, "****\n")
        resultado = partida()
        if resultado == True:
            placar_maquina = placar_maquina + 1
        else:
            placar_jogador = placar_jogador + 1
        rodada = rodada + 1
    print("**** Final do campeonato! ****\n")
    print("Placar: Você", placar_jogador, "X", placar_maquina, "Computador")


escolha = int(input(
"""Bem-vindo ao jogo do NIM! Escolha:
    
1 - para jogar uma partida isolada
2 - para jogar um campeonato """))

if escolha == 1:
    print('\nVoce escolheu uma partida isolada!\n')
    partida()
else:
    print('\nVoce escolheu um campeonato!\n')
    campeonato()

    