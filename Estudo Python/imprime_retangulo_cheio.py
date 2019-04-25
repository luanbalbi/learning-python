def retangulo(larg, alt):
    for h in range(1,alt+1):
        for l in range(1,larg+1):
            print("#",end="")
        print()

def main():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))
    retangulo(largura, altura)

main()
