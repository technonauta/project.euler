#https://projecteuler.net/problem=20
#Factorial digit sum
#Problem 20
#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!


NumerO = int(input("Digite o valor de N: ") )

FatoR=1
for contG in range(1,NumerO+1):
    FatoR *= contG     # == FatoR = FatoR * contG

print(f"Fatorial de N: {FatoR}")

contagem=(tuple(str(FatoR)))
valor=(len(contagem))
soma=0
for cont in range(valor): 
    unidade=(list(contagem[cont])) 
    i=0

    while i < len(unidade):
        soma=soma+int(unidade[i])
        i = i + 1

print(f"soma dos algarismos de N({NumerO})! é: {soma}")