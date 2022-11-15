Algoritmo "problem=3"
//
// Descrição   : https:::projecteuler.net/problem=3
//               Números Primos
// Autor(a)    : Fabiola
// Data atual  : 06-11-2022
//
//  13195 - 5 7 13 29
//  600851475143
// 71 . 839 . 1471 . 6857
Var
         n, valor: real
         cont, m, conttt, mult,r,p:inteiro


Inicio

      escreva("Informe um número inteiro: ")
      leia(n)
      escreva("")
      escreva("limite de tentativas: ")
      leia(m)

      valor<-1
      para cont de 1 ate m faca

          se (n%cont=0) e (valor<=n) entao
            escreval("multiplos :",cont)
            escreva("")

           p<-0
           para mult de 1 ate cont faca

             se (cont%mult=0) entao
                p<-p+1
             fimse
           fimpara
             se (p=2) entao
                escreval("primos :", cont)
             fimse

          valor<-valor*cont
          escreval("valores :", valor)

          fimse


      fimpara
      
Fimalgoritmo



