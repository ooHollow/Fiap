valor = int(input("Insira o ano atual: "))
if valor % 400 == 0 and valor % 100 == 0:
    print("O ano é bissexto")
elif valor % 4 == 0 and valor % 100 >= 1:
    print("O ano é bissexto")
else:
    print("o ano não é bissexto")