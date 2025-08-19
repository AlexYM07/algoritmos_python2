# dada una lista anidada de numeros, devuelve una lista con la suma de cada sublista

def suma_de_listas(lista_anidada):
    suma_lista = [] # lista donde se crea una nueva donde iran las sumas de cada lista
    for sublista in lista_anidada: # recorremos cada sublista
        suma = 0 # variable acumulativa 
        for numero in sublista: # recorremos cada numero de las sublistas para sumarlas
            suma += numero # se ira sumando por listas 
        suma_lista.append(suma) # el total se iran anadiendo a la suma_lista
    return suma_lista

listas = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]
print(suma_de_listas(listas))