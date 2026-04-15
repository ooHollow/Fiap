lista_nome = []
lista_idade = []
i = 0
while i < 10:
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade: "))
    lista_nome.append(nome)
    lista_idade.append(idade)
    i+=1
for nome, idade in zip(lista_nome, lista_idade):
    if idade >= 18:
        print(nome, idade)

for idx, idade in enumerate(lista_idade):
    if idade >= 18:
        print(lista_nome[idx])