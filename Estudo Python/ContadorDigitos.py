numero = int(input("Digite um número inteiro: "))
n = int(input("Digite um número de 0 a 9: "))
resto = 1
quantidade = 0
dividendo = numero

while dividendo != 0:
    resto = dividendo % 10
    if resto == n:
        quantidade = quantidade + 1
    dividendo = dividendo // 10

print("A quantidade de", n, "no número", numero, "é:", quantidade)