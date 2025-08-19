# funcion que suma todos los numeros de una lista anidada

def sumar_lista_aninada(lista_anidada):
    suma = 0 # variable acumulativa
    for sublista in lista_anidada: # recorrer primero las listas
        for numero in sublista: # recorrer los numeros de esas listas
            suma += numero # suma de todos los numeros de todas las listas
    return suma

listas = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]
print(sumar_lista_aninada(listas))