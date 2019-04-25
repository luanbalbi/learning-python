def decompor(num):
    fator = 2
    while num > 1:
        multip = 0
        while num % fator == 0:
            num = num / fator
            multip = multip + 1
        if multip > 0:
            print("Fator", fator, "multiplicidade =", multip)
        fator = fator + 1

    
def main():
    n = 2
    while n > 1:
        n = int(input("Digite um número inteiro(n>1): "))
        if n > 1:
            decompor(n)
        else:
            print("Finalizado")

main()
