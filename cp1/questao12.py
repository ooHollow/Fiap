faltas = int(input("Insira sua porcentagem de faltas na escola: "))
def calculo():
    if faltas > 25:
        print("Você está reprovado.")
        return
    while True:
        nota1 = float(input("Insira sua primeira nota (de 0 a 10): "))
        nota2 = float(input("Insira sua segunda nota (de 0 a 10): "))
        if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
            break
        print("Nota inválida (Insira um número entre 0 e 10).\n")

    media = (nota1 + nota2) / 2
    if media >= 7:
        print("Aprovado.")
    elif 5 <= media < 7:
            print("Em recuperação.")
    elif media < 5:
            print("Reprovado.")
calculo()