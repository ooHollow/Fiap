print("Palestras na região: ")
print("[1] Linux")
print("[2] Banco de Dados")
print("[3] Windows Server")
print("[4] Lógica e Programação")
opcao = int(input("Digite o número da palestra desejada: "))

match opcao:
    case 1:
        print("Essa palestra será realizada no Auditório 1")
    case 2:
        print("Essa palestra será realizada no Auditório 2")
    case 3:
        print("Essa palestra será realizada no Auditório 3")
    case 4:
        print("Essa palestra será realizada no Auditório Principal")