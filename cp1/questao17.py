print("Códigos comuns de HTTP:\n200\n400\n401\n403\n404\n500")
http = int(input("Insira um dos códigos acima: "))
match http:
    case 200:
        print("O código HTTP 200 é a resposta padrão de sucesso.")
    case 400:
        print("O código HTTP 400 significa que o cliente enviou dados invalidos.")
    case 401:
        print("O código HTTP 401 indica que a solicitação não foi processada porque faltam credenciais de autenticação válidas.")
    case 403:
        print("O código de status HTTP 403 indica que o servidor entende a requisição, mas se recusa a autorizá-la.")
    case 404:
        print("O código de status HTTP 404 indica que o servidor web não encontrou a página ou recurso solicitado.")
    case 500:
        print("O Código HTTP 500 indica que o servidor encontrou uma condição inesperada que o impediu de atender à solicitação do cliente.")
    case _:
        print("Codigo não encontrado.")