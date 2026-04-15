nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2026 - nascimento
print("Você tem", idade, "anos")

if idade < 0:
    print("Idade inválida.")
elif idade >= 65:
    print("Você é idoso.")
elif idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")