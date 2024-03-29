#https://projecteuler.net/problem=1
#Multiples of 3 or 5
#Problem 1
#If we list all the natural numbers below 10 that are multiples of
#  3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def main():
    soma=0
    for cont in range(1,1000):
        if cont%3==0 or cont%5==0:
            soma += cont
    print(soma)

main()