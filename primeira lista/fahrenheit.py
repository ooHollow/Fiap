real = int(input("Digite um valor em reais: "))
dollar = real / 5.24
euro = real / 6.07
libras = real / 6.97
iene = real / 0.033
conversor = input("Digite para qual moeda você deseja converter: ")
match conversor:
    case "dollar":
        print(f"O valor {real} em dollar fica {dollar:.2f}")
    case "euro":
        print(f"O valor {real} em euro fica {euro:.2f}")
    case "libras":
        print(f"O valor {real} em libras fica {libras:.2f}")
    case "iene":
        print(f"O valor {real} em iene fica {iene:.2f}")