def triangular(num):
    for i in range(num):
        if i*(i+1)*(i+2) == num:
            return True
    return False