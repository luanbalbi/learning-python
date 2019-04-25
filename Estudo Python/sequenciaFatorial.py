def fatorial(numero):
    fat = 1

    if numero == 0:
        return fat
    else:
        while numero > 0:
            fat = fat * numero
            numero = numero - 1
        return fat

def main():
    print("Calculadora Fatorial\n")
    n = 1
    while n != 0:
        n = int(input("Digite um número inteiro positivo(0=fim): "))
        if n < 0:
            print("Ops! Digite um número positivo ou zero")
        else:
            print("O fatorial de", n, "é", fatorial(n))

main()
