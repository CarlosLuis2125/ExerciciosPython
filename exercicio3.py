#FEITO
import this

this.base = 0
this.altura = 0
this.resultado = 0

def tBase():
    print('Informe o tamanho da base do triângulo')
    this.base = float(input())
    #fim da base

def tAltura():
    print('Informe a altura do seu triângulo')
    this.altura = float(input())
    #fim da altura

def calcular():
    this.resultado = this.base * this.altura
    #fim do calcular
def mostrarResultado():
    tBase()
    tAltura()
    calcular()
    print('A área do seu triângulo é: ' + str(this.resultado))
    #fim do mostrar
