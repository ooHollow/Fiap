valor = float(input("Digite um valor: "))
print("Escolha sua assinatura:")
print("[1] Comum")
print("[2] Funcionário")
print("[3] VIP")
caso = int(input("Digite o número respectivo da sua assinatura: "))

match caso:
    case 1:
        print("O valor pago será de ", valor)
    case 2:
        print("O valor pago será de", valor * 0.95)
    case 3:
        print("O valor pago será de ", valor * 0.9)