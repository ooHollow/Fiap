def analisar_logs(lista_logs):
    resumo = {
        "ERRO": 0,
        "AVISO": 0,
        "INFO": 0
    }
    for n in lista_logs:
        if "[ERRO]" in n:
            resumo["ERRO"] += 1
        elif "[AVISO]" in n:
            resumo["AVISO"] += 1
        elif "[INFO]" in n:
            resumo["INFO"] += 1
    return resumo

log = []
while True:
    entrada = input("Digite o log (ou 'FIM' para encerrar): ")
    if entrada.upper() == "FIM":
        break
    log.append(entrada)

relatorio = analisar_logs(log)

print("\n--- Relatório Final ---")
print(f"Erros: {relatorio['ERRO']}")
print(f"Avisos: {relatorio['AVISO']}")
print(f"Informações: {relatorio['INFO']}")