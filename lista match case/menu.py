print("[1] Picanha        | Valor: 25,00")
print("[2] Lasanha        | Valor: 20,00")
print("[3] Strogonoff     | Valor: 20,00")
print("[4] Bife Acebolado | Valor: 15,00")
print("[5] Pão com Ovo    | Valor:  5,00")
prato = int(input("\nDigite o código do prato desejado: "))

match prato:
    case 1:
        valor = 25
        print("Prato escolhido: Picanha")
    case 2:
        valor = 20
        print("Prato escolhido: Lasanha")
    case 3:
        valor = 20
        print("Prato escolhido: Strogonoff")
    case 4:
        valor = 15
        print("Prato escolhido: Bife Acebolado")
    case 5:
        valor = 5
        print("Prato escolhido: Pão com Ovo")

def pergunta():
    gorjeta = input("Deseja pagar a gorjeta do garçom? [S/N] ").upper()
    if gorjeta == "S":
        print("O total pago será: ", valor + valor * 0.1)
    elif gorjeta == "N":
        print("O total pago será: ", valor)
    else:
        print("Opção invalida.")
        pergunta()
pergunta()