valor = int(input("Digite um valor de 1 a 12: "))
match valor:
    case 1:
        print("Esse valor corresponde a Janeiro. Além disso, esse mês tem 31 dias")
    case 2:
        print("Esse valor corresponde a Fevereiro. Além disso, esse mês tem 28/29 dias")
    case 3:
        print("Esse valor corresponde a Março. Além disso, esse mês tem 31 dias")
    case 4:
        print("Esse valor corresponde a Abril. Além disso, esse mês tem 30 dias")
    case 5:
        print("Esse valor corresponde a Maio. Além disso, esse mês tem 31 dias")
    case 6:
        print("Esse valor corresponde a Junho. Além disso, esse mês tem 30 dias")
    case 7:
        print("Esse valor corresponde a Julho. Além disso, esse mês tem 31 dias")
    case 8:
        print("Esse valor corresponde a Agosto. Além disso, esse mês tem 31 dias")
    case 9:
        print("Esse valor corresponde a Setembro. Além disso, esse mês tem 30 dias")
    case 10:
        print("Esse valor corresponde a Outubro. Além disso, esse mês tem 31 dias")
    case 11:
        print("Esse valor corresponde a Novembro. Além disso, esse mês tem 30 dias")
    case 12:
        print("Esse valor corresponde a Dezembro. Além disso, essse mês tem 31 dias")
    case _:
        print("Valor inválido.")