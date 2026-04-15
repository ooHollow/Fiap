x = input("Qual temperatura deseja utilizar, fahrenheit ou celcius? [F] ou [C]?").upper()
if x == "C":
    i = int(input("Insira a temperatura atual: "))
    i = (i - 32) * 5/9
    print("A temperatura em fahrenheit será igual a: ", i)
elif x == "F":
    i = int(input("Insira a temperatura atual: "))
    i = i * 1.8 + 32
    print("A temperatura em celcius será igual a: ", i)