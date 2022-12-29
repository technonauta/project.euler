#https://projecteuler.net/problem=4
#Largest palindrome product
#Problem 4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit 
# numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def main():

    natural=int(input("Digite um número natural:"))
    natural2=int(input("Digite um número natural:"))
    anterior=1
    for cont in range(100,natural):
        for cont2 in range(100,natural2):
            soluc = cont*cont2

            aux = soluc
            reverso = 0

            while aux != 0:
                reverso = reverso * 10 + aux % 10 # /* acrescenta mais um digito a direita */
                aux = aux // 10                   #  /* joga fora esse digito */
        
            if reverso == soluc and reverso>anterior: #maior número palindromo
                anterior=reverso
                print(f"{cont}*{cont2}=")
                print(soluc)


main()