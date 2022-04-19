#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
#INCOMPLETO
#FALTA CALCULAR PERCENTUAL

import this

this.eleitores = 0
this.vBrancos = 0
this.vNulos = 0
this.vValidos = 0
this.percentual = 0


def eleitores():
    print('Informe o total de eleitores: ')
    this.eleitores = float(input())
    #fim do eleitores

def votosB():
    print('Informe o total de votos brancos: ')
    this.vBrancos = float(input())
    #fim dos votos brancos

def votosN():
    print('Informe o total de votos nulos: ')
    this.vNulos = float(input())
    #fim dos votos nulos

def votosV():
    print('Informe o total de votos válidos: ')
    this.vValidos = float(input())
    #fim dos votos validos

def calcular():
    this.vBrancos = (this.vBrancos / this.eleitores) * 100
    this.vNulos = (this.vNulos / this.eleitores) * 100
    this.vValidos = (this.vValidos / this.eleitores) * 100



def mostrar():
    eleitores()
    votosB()
    votosN()
    votosV()
    print('O percentual de votos brancos em relação com os eleitores: ' + str(this.eleitores) + 'é: ' + str(this.vBrancos) + '%' +
          '\nO percentual de votos nulos em relação com os eleitores: ' + str(this.eleitores) + 'é: ' + str(this.vNulos) + '%' +
          '\nO percentual de votos válidos em relação com os eleitores:' + str(this.eleitores) + 'é: ' + str(this.vValidos) + '%')

