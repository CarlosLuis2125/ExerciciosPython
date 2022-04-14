import this

import exercicio1
import exercicio2

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
            print(exercicio2.coletarNum1())
            #Fim do exercicio2
        elif this.opcao == 0:
            print('Obrigado!')
        else:
            print('Opção inválida! Tente novamente')


