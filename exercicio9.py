#incompleto
import this

this.maca = 0
this.valor = 0
this.total = 0

def quantidadeM():
    print('Informe quantas maçãs você deseja')
    this.maca = float(input())

    if this.maca >= 12:
        this.valor = 1
    else:
        this.maca <= 11
        this.valor = 1.3

def calcular():
    this.total = this.maca * this.valor

def mostrar():
    quantidadeM()
    calcular()
    print('O valor total é de: R$ ' + str(this.total))


