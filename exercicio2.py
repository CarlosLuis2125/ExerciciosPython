#FEITO

import this

this.num1 = 0
this.antecessor = 0



def coletarNum1():
    print('Informe um número')
    this.num1 = float(input())
    #Fim do coletar num1

def mostrarAntecessor():
    coletarNum1()
    this.antecessor = this.num1 - 1

    print('O antecessor de ' + str(this.num1) + ' é: ' + str(this.antecessor))
