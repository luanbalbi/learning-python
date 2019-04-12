def disco():
    i = 1
    maior = 0

    while i <= 31:
        quantidade = int(input("Quantos discos vendidos no dia %d de março? " %i))
        if quantidade > maior:
            maior = quantidade
            dia = i
        i = i + 1

    print("TOP VENDA DE MARÇO")
    print("%d vendas realizadas no dia %d de março de 2019" %(maior, dia))


disco()
