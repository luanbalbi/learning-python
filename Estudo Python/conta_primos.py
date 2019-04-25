def primo(numero):
    num_primo = True
    n = numero - 1
    while (n > 1) and num_primo:
        if (numero % n == 0):
            num_primo = False
        n = n - 1

    if (num_primo == False) or (numero == 1):
        return False
    else:
        return True

def n_primos(n):
    cont = 0
    while n > 1:
        if primo(n):
            cont = cont + 1
        n = n - 1
    return cont
