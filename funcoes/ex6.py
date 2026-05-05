import re
def validarsenha(senha: str):
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%&*]).+$'
    if re.search(padrao, senha):
        return True
    else:
        return False


while True:
    print(validarsenha(input("Digite uma senha: ")))
    if True:
        break
