import this

this.salario = 0
this.vendas = 0
this.valor = 0
this.adicional = 0

def salario():
    print('Informe o salário fixo do vendedor')
    this.salario = float(input())

def vVendas():
    print('Informe o valor das vendas')
    this.vendas = float(input())

def calcular():
    if this.vendas <= 1500:
        this.adicional = ((this.vendas * 3) / 100)
    else:
        this.adicional = ((this.vendas * 5) / 100)

    this.total = this.adicional + this.salario

def mostrar():
    salario()
    vVendas()
    calcular()
    print('Novo salário ' + str(this.total))