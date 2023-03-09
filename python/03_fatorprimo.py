#https://projecteuler.net/problem=3
#Largest prime factor
#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def main():

    n = int(input("Digite um numero (>1): "))

    fator = 2 # primeiro fator
    mult = 0;

    while n != 1:
        # conta a multiplicidade de fator em n
        if n%fator == 0:
            n = n / fator;
            mult = mult + 1;
        else:
            # imprime a multiplicade do fator
            if mult != 0:
                print("fator %d multiplicidade1 %d" %(fator, mult))
                mult = 0

            fator = fator + 1

    # imprime a multiplicade do ultimo fator
    if mult != 0:
        print("fator %d multiplicidade2 %d" %(fator, mult))

main() # chamada da função principal