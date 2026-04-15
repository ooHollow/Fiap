nome = input("Insira seu nome: ")
peso = int(input("Insira seu peso em (Em KG): "))
altura = float(input("Insira sua altura (Em Metros): "))
imc = peso/(altura*altura)
if imc < 18.5:
    print(f'seu imc é: {imc:.2f}. Além disso, você está abaixo do peso')
elif 18.5 < imc < 25:
    print(f'seu imc é: {imc:.2f}. Além disso, você está normal')
elif 25 < imc < 30:
    print(f'seu imc é: {imc:.2f}. Além disso, você está com sobrepeso')
elif 30 < imc < 35:
    print(f'seu imc é: {imc:.2f}. Além disso, você está com obesidade grau 1')
elif 35 < imc < 40:
    print(f'seu imc é: {imc:.2f}. Além disso, você está com obesidade grau 2')
elif 40 < imc:
    print(f'seu imc é: {imc:.2f}. Além disso, você está com obesidade grau 3')