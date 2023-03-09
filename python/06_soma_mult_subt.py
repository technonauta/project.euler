#https://projecteuler.net/problem=6
#Sum square difference
#Problem 6
#The sum of the squares of the first ten natural numbers is,
#1²+2²....+10²= 385

#The square of the sum of the first ten natural numbers is,
#(1+2...+10)²= 55² = 3025

#Hence the difference between the sum of the squares of the 
# first ten natural numbers and the square of the sum is 
#3025-385=2640

#Find the difference between the sum of the squares of the 
#first one hundred natural numbers and the square of the sum.

def main():
    numtotalquad=int(input("digite número máximo: "))
    totalsoma=0

    for cont in range(1,numtotalquad):
        total=cont**2
        totalsoma += total
    print(f"soma dos quadrados: {totalsoma}")

    somacontd=0
    somacont = 0

    for cont in range(1,numtotalquad):
        somacontd += cont
        somacont = somacontd**2
    print(f"quadrado da soma: {somacont}")

    resposta = somacont - totalsoma
    print(f"resposta subtração: {resposta}")


main()