a = int(input("Insira o primeiro lado: "))
b = int(input("Insira o segundo lado: "))
c = int(input("Insira o terceiro lado: "))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("equilátero")
    elif a == b or a == c or b == c:
        print("isósceles")
    else:
        print("escaleno")
else:
    print("esse triangulo nem existe")