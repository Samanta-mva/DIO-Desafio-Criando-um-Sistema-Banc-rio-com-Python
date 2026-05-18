def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def exibir_resultado(a,b,operacao):
    resultado = operacao(a,b)
    if operacao == somar: nome = 'soma'
    elif operacao == subtrair: nome = 'subtração'
    print(f'O resultado da operacao de {nome} entre {a} e {b} é igual a {resultado}')

exibir_resultado(3,2,somar)
exibir_resultado(3,2,subtrair)


# podemos usar também desta outra forma
op = somar
print(op(5,13))