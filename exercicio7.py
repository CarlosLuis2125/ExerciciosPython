#feito
import this

this.carro = 0
this.fabrica = 0
this. imposto = 0
this.distribuidor = 0

def custo():
    print('Informe o custo de fabrica do veículo: ')
    this.fabrica = float(input())

def calcular():
    this.imposto = this.fabrica * 45 / 100
    this.distribuidor = this.fabrica * 28 / 100
    this. carro = this.imposto + this.distribuidor + this.fabrica

def mostrar():
    custo()
    calcular()
    print('O valor total do carro é: ' + str(this.carro))