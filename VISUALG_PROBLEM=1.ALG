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

     se (i%3=0) ou (i%5=0) entao
       soma <- soma + i
     fimse

   fimpara

   escreval(soma)

Fimalgoritmo



