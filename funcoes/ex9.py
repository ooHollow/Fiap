def sacar(valor: int):
    if valor < 2 or valor == 3:
        print("Valor indisponível.")
        return
    nota5 = 0
    if valor % 2 != 0:
        nota5 = 1
        valor -= 5
    nota100, restante = divmod(valor, 100)
    nota50, restante = divmod(restante, 50)
    nota20, restante = divmod(restante, 20)
    nota10, restante = divmod(restante, 10)
    nota2, restante = divmod(restante, 2)
    return nota100, nota50, nota20, nota10, nota5, nota2