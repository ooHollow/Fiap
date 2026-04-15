lista = []

while True:
    nota = float(input("Insira a nota do aluno: "))
    if nota == 0:
        break
    lista.append(nota)

print(len(lista))
print(lista)
media = sum(lista) / len(lista)
print(media)
notas_acima_media = []
for n in lista:
    if n > media:
        notas_acima_media.append(n)
print(notas_acima_media)