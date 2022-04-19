#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
#FALTA CALCULAR MEDIA


import this
this.notaUm = 0
this.notaDois = 0
this.notaTres = 0
this.media = 0


def nota1():
    print('Informe a primeira nota do aluno: ')
    notaUm = float(input())
    #fim do nota1

def nota2():
    print('Informe a seguunda nota do aluno: ')
    this.notaDois = float(input())
    #fim do nota2

def nota3():
    print('Informe a terceira nota do aluno: ')
    this.notaTres = float(input())
    #fim do nota3

def calcular():
    this.media = (this.notaUm + this.notaDois + this.notaTres) / 3
    #fim do calcular

def mostrar():
    nota1()
    nota2()
    nota3()
    calcular()
    print('A média do aluno é: ' + str(this.media))