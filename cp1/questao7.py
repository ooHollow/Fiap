idade = int(input("Insira sua idade: "))
ano = int(input("Insira por quantos anos você contribuiu: "))

if idade >= 65 or ano >= 30 or idade >= 60 and ano >= 25:
    print("Você está apto a se aposentar.")
else:
    print("Você não está apto a se aposentar.")