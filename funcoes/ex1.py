def soma(a, b ,c):
    if a + b == c:
        return True
    elif b + c == a:
        return True
    elif a + c == b:
        return True
    else:
        return False