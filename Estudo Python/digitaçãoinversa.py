lista = []
fim = False

while not fim:
    lista.append(int(input("Digite um número inteiro(0=fim): ")))
    if lista[-1] == 0:
        fim = True        

cont = 1
while cont <= len(lista):
    print(lista[-cont])
    cont = cont + 1
    
