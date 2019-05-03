def verif_primo(numero):
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

def maior_primo(x):
    maiorprimo = False
    while (x > 1) and (not maiorprimo):
        if verif_primo(x) == True:
            maiorprimo == True
            return x
        else:
            x = x - 1