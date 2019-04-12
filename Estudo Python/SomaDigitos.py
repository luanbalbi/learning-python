numero = int(input("Digite um número inteiro: "))
resto = 1
soma = 0
dividendo = numero

while dividendo != 0:
    resto = dividendo % 10
    soma = soma + resto
    dividendo = dividendo // 10

print("A soma dos dígitos é:", soma)