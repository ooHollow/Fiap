def solution(string: str, num: int):
    resultado = ""
    for n in range(0, len(string)):
        if 'a' <= string[n] <= 'z':
            char = chr((ord(string[n]) - 97 + num) % 26 + 97)
            resultado += char
        elif 'A' <= string[n] <= 'Z':
            char = chr((ord(string[n]) - 65 + num) % 26 + 65)
            resultado += char
        elif '0' <= string[n] <= '9':
            char = chr((ord(string[n]) - 48 + num) % 10 + 48)
            resultado += char
        else:
            resultado += string[n]
    return resultado