#FEITO
import this
this.numA = 10
this.numB = 20
this.numC = 0

def coletarA():
    print('Informe um número para representar A')
    this.numA = float(input())

def coletarB():
    print('Informe outro número para representar B')
    this.numB = float(input())

def inverter():
    this.numC = this.numB
    this.numB = this.numA
    this.numA = this.numC

def mostrar():
    coletarA()
    coletarB()
    inverter()
    print('O valor de A é: ' + str(this.numA) + '\nO valor de B é: ' + str(this.numB))
