import math

x1 = int(input("Digite a coordenada de X do primeiro ponto: "))
y1 = int(input("Digite a coordenada de Y do primeiro ponto: "))
x2 = int(input("Digite a coordenada de X do segundo ponto: "))
y2 = int(input("Digite a coordenada de Y do segundo ponto: "))

distX = (x2 - x1) ** 2

distY = (y2 - y1) ** 2

distancia = math.sqrt(distX + distY)


if distancia >= 10:
    print("longe")
else:
    print("perto")
