n = 0

while n <= 0:
    n = int(input("Informe um número positivo para calcularmos o n-ésimo número da sequência de Fibonacci: "))
    if n <= 0:
        print("ERRO: Digite apenas números maiores que 0 (zero)!!!\n")
        
i = 1
seq_F = ""
Fant = 0
Fatual = 1


while i < n:
    Fprox = Fant + Fatual
    Fant = Fatual
    Fatual = Fprox
    i = i + 1
    seq_F = seq_F + str(Fatual) + " "

if n > 1:
    seq_F = "1 " + seq_F
else:
    seq_F = "1"

print("O %dº número da sequência de Fibonacci é %d" %(n, Fatual))
print("Sequência inteira até o número informado:", seq_F)
