# funcion que dada una lista de numeros, 
# devolvera una lista con los maximos de cada sublista
"""
solucion pero sin funcion max()

listas = [
    [1, 2, 3],
    [3, 4],
    [6, 7, 8, 9]
]

lista_maximos = []

for sublista in listas: # recorremos las listas
    maximo = sublista[0] # asumimos que el primer es el maximo
    for numero in sublista: # recorremos cada sublista sus numeros
        if numero > maximo: 
            maximo = numero # actulizamos si encontramos uno mayor en cada lista
    lista_maximos.append(maximo) # se vayan anadiendo a la lista
    
print(lista_maximos)

"""
def maximos(lista_anidada):
    lista_maximos = []
    for sublista in lista_anidada:
        lista_maximos.append(max(sublista))
    return lista_maximos

listas = [
    [1, 2, 3],
    [3, 4],
    [6, 7, 8, 9]
]

print(maximos(listas))
