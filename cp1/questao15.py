valor = int(input("Insira o valor a ser sacado: "))
if valor <= 0 or valor == 1 or valor == 3:
    print("Valor indisponível.")
else:
    if valor % 2 != 0:
        nota5 = 1
        valor -= 5
    print("Saque realizado com sucesso.")
    nota100, restante = divmod(valor, 100)
    print(f'Notas de 100: {nota100}')
    nota50, restante = divmod(restante, 50)
    print(f'Notas de 50: {nota50}')
    nota20, restante = divmod(restante, 20)
    print(f'Notas de 20: {nota20}')
    nota10, restante = divmod(restante, 10)
    print(f'Notas de 10: {nota10}')
    nota2, restante = divmod(restante, 2)
    print(f'Notas de 2: {nota2}')