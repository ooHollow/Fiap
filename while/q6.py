list = []
while True:
    x = int(input("Digite números: "))
    list.append(x)
    if x == 0:
        break
print(sum(list))