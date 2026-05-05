def solution(string: str):
    if not string:
        return ""
    lista = []
    prev_char = string[0]
    count = 1
    for n in string[1:]:
        if n == prev_char:
            count += 1
        else:
            lista.append(f"{prev_char}{count}")
            prev_char = n
            count = 1
    lista.append(f"{count}{prev_char}")
    return "".join(lista)
print(solution("AAAABBBCCDAA"))