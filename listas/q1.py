i = 0
par = []
impar = []
while i < 10:
    x = int(input())
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
    i+=1
print(par)
print(impar)