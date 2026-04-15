valor = float(input("Fala ai quanto tu tem que pagar: "))
print("\nopções")
print("1 - PIX")
print("2 - Crédito")
print("3 - Crédito parcelado")
escolha = int(input("escolhe uma ai: "))

match escolha:
    case 1:
        print(f'paga ai {valor * 0.9}')
    case 2:
        print(f'paga ai {valor}')
    case 3:
        print(f'paga ai {valor * 1.05}')