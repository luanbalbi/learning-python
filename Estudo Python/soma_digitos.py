numero = int(input("Digite um número inteiro: "))
soma = 0

while numero > 0:
    digito = numero % 10
    soma = soma + digito
    numero = numero // 10

print(soma)
