def primo(numero):
    num_primo = True
    n = numero - 1
    while (n > 1) and num_primo:
        if (numero % n == 0):
            num_primo = False
        n = n - 1

    if (num_primo == False) or (numero == 1):
        print(numero, "não é primo.")
    else:
        print(numero, "é primo!")

def main():
    n = 1
    while n > 0:
        n = int(input("Digite um número inteiro(n>0): "))
        if n > 0:
            primo(n)
        else:
            print("Finalizado")

main()
