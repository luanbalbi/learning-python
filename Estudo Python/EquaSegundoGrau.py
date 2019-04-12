import math

print("==== Calculadora de equação do segundo grau ====")
print()
print("Modelo de equação: ax² + bx + c = 0")
print()
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b ** 2) - (4 * a * c)

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("As duas raízes reais da equação %dx²+%dx+%d=0 são:" %(a, b, c))
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A única raíz real da equação %dx²+%dx+%d=0 é:" %(a, b, c))
    print("x1 =", x1)
else:
    print("A equação %dx²+%dx+%d=0 não possui raízes reais" %(a, b, c))
