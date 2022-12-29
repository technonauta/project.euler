#https://projecteuler.net/problem=2
#Even Fibonacci numbers
#Problem 2
#Each new term in the Fibonacci sequence is generated by adding 
# the previous two terms. By starting with 1 and 2, the first 10 
# terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.

def main():
    print("Sequência de Fibonacci")

    numene=int(input("Digite um número: ")) #posição do número Fibonacci
    #1   2   3   4   5   6    7   8    9
    #1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34
    #fibo >> número fibonacci

    f1=1
    f2=1
    soma=0

    if (numene==1) or (numene==2):
        print(f"{1}")
    
    else:
        for contad in range(2,numene):
            fibo=f1+f2
            f1=f2
            f2=fibo
    
            if fibo %2 ==0:
                soma += fibo

        print("F(%d) = %d" %(numene,fibo))
        print(f"soma números pares: {soma}")


main()
