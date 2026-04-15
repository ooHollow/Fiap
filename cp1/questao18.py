valor = int(input("Digite um valor em reais: "))

dolar = valor / 5.2
euro = valor / 6
libras = valor / 6.9
iene = valor / 0.03

conversor = input("-Opções-\nDolar\nEuro\nLibras\nIene\nInsira a opção para converter: ").lower()
match conversor:
    case "dolar":
        print(f'O valor {valor} em dollar fica {dolar:.2f}')
    case "euro":
        print(f'O valor {valor} em euro fica {euro:.2f}')
    case "libras":
        print(f'O valor {valor} em libras fica {libras:.2f}')
    case "iene":
        print(f'O valor {valor} em iene fica {iene:.2f}')
    case _:
        print("Opção invalida.")