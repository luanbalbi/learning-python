def inverter(lista):
    for i in range(len(lista),0,-1):
        print(lista[i-1])

def main():
    lista = []
    lista.append(int(input("Digite um número: ")))
    while lista[-1] != 0:
        lista.append(int(input("Digite um número: ")))
    del lista[-1]
    inverter(lista)


main()