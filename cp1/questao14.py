def myfunc(dia, mes, ano):
    lista = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if ano % 400 == 0 and ano % 100 == 0 or ano % 4 == 0 and ano % 100 >= 1:
        lista[1] = 29
    if 1 <= mes <= 12 and 1 <= dia <= lista[mes - 1]:
        print("Data valida.")
    else:
        print("Data invalida.")
myfunc(int(input("Insira o dia: ")), int(input("Insira o mês: ")), int(input("Insira o ano (Ex: 2008): ")),)