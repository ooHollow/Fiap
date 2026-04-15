c, j, i = 1.5, 1.1, 0
while c >= j:
    print(f'c - {c:.2f}, j - {j:.2f}')
    c+=0.02; j+=0.05; i+=1
print("Total", i)