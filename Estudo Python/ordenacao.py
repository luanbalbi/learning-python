numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

if (numero3 > numero2) and (numero2 > numero1):
    print("crescente")
else:
    print("não está em ordem crescente")
