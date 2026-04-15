opcao = int(input("====Opções de veiculos====\n[1] - carro\n[2] - moto\n[3] - ônibus\n[4] - caminhão\nInsira um valor correspondente ao veiculo desejado: "))
match opcao:
    #inventei os valores
    case 1:
        print("O valor do pedágio do carro será de 5 reais.")
    case 2:
        print("O valor do pedágio da moto será de 3 reais.")
    case 3:
        print("O valor do pedágio do ônibus será de 10 reais.")
    case 4:
        eixos = int(input("Quantos eixos o caminhão possui? (de 1 a 6): "))
        match eixos:
            case 1:
                print("O pedágio será de 5 reais.")
            case 2:
                print("O pedágio será de 6 reais.")
            case 3:
                print("O pedágio será de 7 reais.")
            case 4:
                print("O pedágio será de 8 reais.")
            case 5:
                print("O pedágio será de 9 reais.")
            case 6:
                print("O pedágio será de 10 reais.")
            case _:
                print("Valor inválido.")
    case _:
        print("Valor inválido.")