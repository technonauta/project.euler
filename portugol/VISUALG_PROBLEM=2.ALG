Algoritmo "problem=2"
//
//
// Descrição   : https:::projecteuler.net/problem=2
// Fibonacci
// Autor(a)    : Fabiola
// Data atual  : 05-11-2022
//
//
Var
     v1, v2, v3, cont, sum, limite: real

Inicio

        v1<-0
        v2<-1
        cont<-1

        enquanto v3<3999999 faca
          v3<-v1+v2
          v1<-v2
          v2<-v3

           se (v3%2=0) entao
              sum<-sum+v3
           fimse

fimenquanto
        
        escreva(sum, "   soma total")
        
Fimalgoritmo



