def fatorial(n):
    fat = 1
    while n > 0:
        fat = fat * n
        n = n - 1
    return fat

###
def testa_fatorial():
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")
###

def numero_binominal(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n-k))

        
n = int(input("Digite valor de n: "))
k = int(input("Digite valor de k: "))

print(numero_binominal(n, k))

