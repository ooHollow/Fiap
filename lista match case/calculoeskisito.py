numero = float(input("Digite um numero inteiro: "))
print("Dentre as seguintes opções escolha uma: ")
print("[1] Dobrar")
print("[2] Dividir por 2")
print("[3] 1/10 do numero")
opcao = int(input("Digite o numero da opção desejada: "))

match opcao:
    case 1:
        print(numero * 2)
    case 2:
        print(numero / 2)
    case 3:
        print(numero * 0.1)