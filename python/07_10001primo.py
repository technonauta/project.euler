#https://projecteuler.net/problem=7
#10001st prime
#Problem 7
#By listing the first six prime numbers: 
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

#https://pt.stackoverflow.com/questions/456846/n%C3%BAmeros-primos-com-while-e-for

def main():
    print("Número primo")
    asaber=int(input("Digite: ")) #105.000
    soma=0 #9933
    for i in range(2,asaber): #104000
        j = 2
        counter = 0
        while j < i:
            if i % j == 0:
                counter = 1
                j = j + 1
            else:
                j = j + 1

        if counter == 0:
            print(str(i) + " é um número primo")
            soma+=1
            counter = 0
            if soma==10001:
                print(f"POSIÇÃO 10001 {i}")
        
        else:
            counter = 0
    
    print(f"o número {i} tá na posição: {soma}")
main()

#1 ate 104.000 > 9933 posições
