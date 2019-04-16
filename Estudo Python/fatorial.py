numero = int(input("Digite o valor de n: "))
fatorial = 1

if numero == 0:
    fatorial = 1
else:
    while numero > 0:
        fatorial = fatorial * numero
        numero = numero - 1

print(fatorial)
