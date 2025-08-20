# dada una lista anidada de numeros, crear una funcion que devuelva una lista 
# con los numeros pares de cada sublista
def pares_lista_anidada(lista_anidada):
    lista_pares = [] # lista para los pares 
    for sublista in lista_anidada: # para oder recorrer las listas
        for numero in sublista: # recorrer los numeros dentro de las listas
            if numero % 2 == 0: # si el resultado da 0 entonces es par
                lista_pares.append(numero) # si es par pues se anade a la lista
    
    return lista_pares

listas = [
    [1, 2, 3],
    [4, 8],
    [9, 7 , 10]
]

print(pares_lista_anidada(listas))


# si queremos que cada sublista tenga solo sus pares 
def pares_lista_aniada_sublistas(lista_anidada):
    lista_pares = [] # lista final 
    for sublista in lista_anidada: # recorremos cada sublista
        pares_sublista = [] # lista para los pares de esta sublista
        for numero in sublista:
            if numero % 2 == 0:
                pares_sublista.append(numero)
        lista_pares.append(pares_sublista) # agregamos los pares de esta sublista
    return lista_pares

listas = [
    [1, 2, 3],
    [4, 8],
    [9, 7, 10]
]
print(pares_lista_aniada_sublistas(listas))