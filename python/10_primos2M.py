#https://projecteuler.net/problem=10
#Summation of primes
#Problem 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#https://codereview.stackexchange.com/questions/132343/project-euler-10-find-the-sum-of-all-the-primes-below-two-million

def eratosthenes2(n):
    #Declare a set - an unordered collection of unique elements
    multiples = set()

    #Iterate through [2,mudarval]
    for i in range(2, n+1):

        #If i has not been eliminated already 
        if i not in multiples:

            #Yay prime!
            yield i

            #Add multiples of the prime in the range to the 'invalid' set
            multiples.update(range(i*i, n+1, i))

#Now sum it up
iter = 0
mudarval=int(input("digite valor: "))

ml = list(eratosthenes2(mudarval))

for x in ml:
    
    iter += int(x)

print(iter)