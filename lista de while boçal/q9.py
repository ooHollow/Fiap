l = [int(input("Digite um numero: ")) for _ in range(int(input("Quantos números? ")))]
print(sum(i := [n for n in l if n % 2]) / len(i), sum(p := [n for n in l if not n % 2]) / len(p))