def eh_primo(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for k in range(3, n//2+1):
            if n % k == 0:
                return False
        return True


def lista_primos():
    lista = []
    for i in range(2, 524):
        if eh_primo(i):
            lista.append(i)
    print(lista)


lista_primos()
