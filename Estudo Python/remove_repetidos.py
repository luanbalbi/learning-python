def remove_repetidos(lista):
    x_cont = 0
    tam_lista = len(lista)
    while x_cont < tam_lista:
        x = lista[x_cont]
        y_cont = 0
        while y_cont < tam_lista:
            y = lista[y_cont]
            if x == y and x_cont != y_cont:
                del lista[y_cont]
                tam_lista = tam_lista - 1
            else:
                y_cont = y_cont + 1
        x_cont = x_cont + 1
    lista.sort()
    return lista