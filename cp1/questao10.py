x = int(input("Insira o x: "))
y = int(input("Insira o y: "))
if x == 0 and y == 0:
    print("O ponto está no local de origem.")
elif x == 0 and y > 0:
    print("O ponto está no eixo y")
elif x > 0 and y == 0:
    print("O ponto está no eixo x")
elif x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 < y:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 > y:
    print("O ponto está no quarto quadrante.")