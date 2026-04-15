def jogo():
    escolha1 = input("Jogador 1 - Escolha entre pedra, papel ou tesoura [PEDRA, PAPEL, TESOURA]: ").upper()
    escolha2 = input("Jogador 2 - Escolha entre pedra, papel ou tesoura [PEDRA, PAPEL, TESOURA]: ").upper()
    if escolha1 == "PEDRA" and escolha2 == "TESOURA":
        print("Jogador 1 venceu")
    elif escolha1 == "TESOURA" and escolha2 == "PEDRA":
        print("Jogador 2 venceu")
    elif escolha1 == "TESOURA" and escolha2 == "PAPEL":
        print("Jogador 1 venceu")
    elif escolha1 == "PAPEL" and escolha2 == "TESOURA":
        print("Jogador 2 venceu")
    elif escolha1 == "PAPEL" and escolha2 == "PEDRA":
        print("Jogador 1 venceu")
    elif escolha1 == "PEDRA" and escolha2 == "PAPEL":
        print("Jogador 2 venceu")
    elif escolha1 == "PEDRA" == escolha2:
        print("Empate. Tente novamente")
        jogo()
    elif escolha1 == "PAPEL" == escolha2:
        print("Empate. Tente novamente")
        jogo()
    elif escolha1 == "TESOURA" == escolha2:
        print("Empate. Tente novamente")
        jogo()
jogo()