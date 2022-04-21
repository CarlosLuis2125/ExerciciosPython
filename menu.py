import this

import exercicio1
import exercicio11
import exercicio13
import exercicio2
import exercicio3
import exercicio4
import exercicio5
import exercicio6
import exercicio7
import exercicio8
import exercicio9

this.opcao = -1
num1 = 0

def exercicioUm():
    this.numA = 10
    this.numB = 20
    this.numC = 0

    this.numA = this.numB
    this.numB = this.numA
    this.numB = this.numC

    return this.numA, this.numB, this.numC

def mostrarMenu():
    print('Escolha um dos exercícios abaixo: ' +
          '\n1. Exercício 1' +
          '\n2. Exercício 2' +
          '\n3. Exercício 3' +
          '\n4. Exercício 4' +
          '\n5. Exercício 5' +
          '\n6. Exercício 6' +
          '\n7. Exercício 7' +
          '\n8. Exercício 8' +
          '\n9. Exercício 9' +
          '\n10. Exercício 10' +
          '\n11. Exercício 11' +
          '\n13. Exercício 13' +


          '\n0. Sair')

    this.opcao =int(input())#Coletar a digitação do usuário

def operacoes():
    #Mostrar menu em tela

        mostrarMenu()
        #realizar operações
        if this.opcao == 1:
            print(exercicio1.mostrar())
            #Fim do exercicio 1
        elif this.opcao == 2:
            print(exercicio2.mostrarAntecessor())
            #Fim do exercicio2
        elif  this.opcao == 3:
            print(exercicio3.mostrarResultado())
            #fim do opcao3
        elif this.opcao == 4:
            print(exercicio4.mostrar())
        elif this.opcao == 5:
            print(exercicio5.calcular())
            #fim do this.opcao5
        elif this.opcao == 6:
            print(exercicio6.calcular())
        elif this.opcao == 7:
            print(exercicio7.mostrar())
        elif this.opcao == 8:
            print(exercicio8.mostrar())
        elif this.opcao == 9:
            print(exercicio9.mostrar())
        #elif this.opcao == 10:
        #    print(exercicio10.)
        elif this.opcao == 11:
            print(exercicio11.mostrar())
        elif this.opcao == 13:
            print(exercicio13.mostrar())
        elif this.opcao == 0:
            print('Obrigado!')
        else:
            print('Opção inválida! Tente novamente')


