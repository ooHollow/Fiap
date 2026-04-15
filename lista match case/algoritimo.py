numero = int(input("Digite um numero inteiro: "))
calculo = numero % 3

match calculo:
    case 0:
        print("O valor digitado é divisivel por 3")
    case _:
        print("O valor digitado não é divisivel por 3")