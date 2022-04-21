#feito
import this

this.ano = 0
this.meses = 0
this.dias = 0
this.total = 0

def anos():
    print('Quantos anos você tem?')
    this.ano = float(input())

def meses():
    print('Quantos meses?')
    this.meses = float(input())

def dias():
    print('Quantos dias?')
    this.dias = float(input())

def calcular():
    this.total = (this.ano * 365) + (this.meses * 30) + this.dias

def mostrar():
    anos()
    meses()
    dias()
    calcular()
    print('A sua idade em dias é: ' + str(this.total))