salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500)
print(salario_com_bonus,'\n')

# outro exemplo usando listas
def numeros(lista):
    #desta forma alteramos a lista original
    lista.append(2)
    print(f'Lista aterada {lista}')

lista = [1]
numeros(lista)
print(f'Lista original {lista}\n')


def numeros2(lista2):
    lista2_aux = lista2.copy()
    lista2_aux.append(2)
    print(f'Lista 2 alterada {lista2_aux}')

lista2 = [1]
numeros2(lista2)
print(f'LIsta 2 original {lista2}')