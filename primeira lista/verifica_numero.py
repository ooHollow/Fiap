#define o numero
numero = int(input("Digite um número: "))

#testa se é par ou impar

print("O número escolhido é par." if numero % 2 == 0 else "O número escolhido é impar.")

if numero < 0:
    print("Além disso, o número escolhido é negativo.")
elif numero == 0:
    print("Além disso, o número escolhido é igual a zero.")
else:
    print("Além disso, o número escolhido é positivo.")