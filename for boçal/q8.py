n = int(input())
i = 2
x = 0
for i in range(i, n):
    if n % i == 0:
        x+=1
        break
if x == 0:
    print("primo")
else:
    print("nao primo")