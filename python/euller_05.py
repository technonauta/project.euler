#https://projecteuler.net/problem=5
#Smallest multiple
#Problem 5
#2520 is the smallest number that can be divided by each of the 
# numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

#https://pt.stackoverflow.com/questions/292553/como-implementar-um-algoritmo-de-c%C3%A1lculo-de-mdc-recursivo-em-python

from math import gcd

def mmc(numeros):
    m = 1
    for n in numeros:
        m = m * n // gcd(m, n)
    return m

print(mmc([11, 13, 14, 15, 16, 17, 18, 19, 20]))

###########################################
# A partir de Python 3.9
#https://pt.stackoverflow.com/questions/439722/obter-o-menor-n%C3%BAmero-positivo-que-%C3%A9-divis%C3%ADvel-por-todos-os-n%C3%BAmeros-de-1-a-20
#least common multiple

from math import lcm

print(lcm(11, 13, 14, 15, 16, 17, 18, 19, 20)) # 232792560

##################################