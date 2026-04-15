valor = int(input("Insira a quantidade de segundos que deseja converter: "))
horas = valor // 3600
restante = valor % 3600
minutos = restante // 60
segundos = restante % 60
print(f'{horas}h {minutos}m {segundos}s')