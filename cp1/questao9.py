num1 = float(input("Insira o primeiro valor: "))
num2 = float(input("Insira o segundo valor: "))

def operacao():
    operador = input("Insira o operador que deseja usar (*, /, +, -): ")
    if operador == "+":
        print(num1 + num2)
    elif operador == "-":
        print(num1 - num2)
    elif operador == "*":
        print(num1 * num2)
    elif operador == "/":
        if num1 == 0 or num2 == 0:
            print("Um dos valores é zero. Não será possivel realizar a operação.")
        else:
            print(num1 / num2)
    else:
        print("operador inválido.")
        operacao()
operacao()