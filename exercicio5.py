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
    eleitores()
    votosB()
    votosN()
    votosV()

    print('A quantidade de votos brancos é de ' + str(this.vBrancos) + 'e a porcentagem que representa é de: ' + str(((this.vBrancos / eleitores) * 100)) + '% do total')
    print('A quantidade de votos nulos é de ' + str(this.vNulos) + 'e a porcentagem que representa é de: ' + str(((this.vNulos / eleitores) * 100)) + '% do total')
    print('A quantidade de votos nulos é de ' + str(this.vValidos) + 'e a porcentagem que representa é de: ' + str(((this.vValidos / eleitores) * 100)) + '% do total')
