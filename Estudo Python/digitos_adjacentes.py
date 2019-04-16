adjacente = False
numero = int(input("Digite um número inteiro: "))
if numero < 0:
    prox_dividendo = numero * (-1)
else:
    prox_dividendo = numero

             
while (prox_dividendo != 0) and (not adjacente):
    verif_1 = prox_dividendo % 10
    prox_dividendo = prox_dividendo // 10
    verif_2 = prox_dividendo % 10
    if (verif_1 == verif_2):
        adjacente = True

if (adjacente == False):
    print("não")
else:
    print("sim")
