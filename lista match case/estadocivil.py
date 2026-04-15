print("Identifique nas opções abaixo seu estado civil")
print("1 - S")
print("2 - C")
print("3 - V")
print("4 - D")

opcao = int(input("Escolha uma das opções acima: "))

match opcao:
    case 1:
        print("Você é solteiro.")
    case 2:
        print("Você é casado.")
    case 3:
        print("Você é viúvo.")
    case 4:
        print("Você é divorciado.")
    case _:
        print("Opção invalida.")