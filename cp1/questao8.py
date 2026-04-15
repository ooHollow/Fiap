salario = float(input("Insira seu salário bruto: "))
if salario <= 2112:
    print("Isento.")
elif 2112 < salario < 2865.65:
    print(f'você recebe {salario * 0.925}')