num_primo = True
numero = int(input("Digite um número inteiro: "))
n = numero - 1
while (n > 1) and num_primo:
    if (numero % n == 0):
        num_primo = False
    n = n - 1

if (num_primo == False) or (numero == 1):
    print("não primo")
else:
    print("primo")
