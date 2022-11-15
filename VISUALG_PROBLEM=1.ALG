Algoritmo "problem=1"
// 
//  
// Descrição   : https:::projecteuler.net/problem=1
// Autor(a)    : Fabiola
// Data atual  : 05-11-2022
//
//
Var
   N3, i, N5, soma3, soma5, soma : inteiro
   vet3: vetor [1..334] de inteiro
   vet5: vetor [1..200] de inteiro


Inicio
   escreval("Qual a soma dos multiplos de 3 e 5 até abaixo de 1000? ")
   leia(N3)

   soma3<-0
   para i de 1 até 333 faca
           vet3[i] <- N3*i
           se vet3[i]%5 <>0 entao
            soma3 <- soma3 + vet3[i]
           fimse
   fimpara

   escreval("resultado 3", soma3)


   escreval("Qual a soma dos multiplos de 3 e 5 até abaixo de 1000? ")
   leia(N5)

   soma5<-0
   para i de 1 até 199 faca
           vet5[i] <- N5*i
           soma5 <- soma5 + vet5[i]
   fimpara

   escreval("resultado 5", soma5)

   soma<- soma3+soma5


   escreval("SOMA TOTAL", soma)

Fimalgoritmo


Algoritmo "problem=1"
//
//
// Descrição   : https:::projecteuler.net/problem=1
// Autor(a)    : Fabiola
// Data atual  : 05-11-2022
//
//
Var
     soma, i: inteiro

Inicio

   para i de 1 ate 999 faca

     se (i%3=0) entao
       soma <- soma + i
     fimse

     se (i%5=0) entao
       soma <- soma + i
     fimse

     se (i%15=0) entao
       soma <- soma - i
     fimse

   fimpara


   escreval(soma)


Fimalgoritmo



