# dada una lista nidada de numeros, crea una funcion que devuelva una lista 
# con el promedio (media) de cada sublista.
def promedio_anidadas(lista_anidada):
    lista_promedios = [] # lista para los promedios
    for sublista in lista_anidada: # recorremos las listas
        suma = 0 
        promedio = 0 
        for numero in sublista: # recorremos los numeros de las sublistas unas por una
            suma = numero + suma # sumamos cada lista 
        promedio = suma / len(sublista) # promedio de cada lista, lo calculamos al final (eficiencia y logica)
        lista_promedios.append(promedio) # append para ponerlas en la lista_promedios
        
    return lista_promedios


listas = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]

print(promedio_anidadas(listas))

'''
esta es otra version del codigo mas corta y una funcion 
...
def promedio_anidadas(lista_anidada):
    lista_promedios = []
    for sublista in lista_anidada:
        promedio = sum(buslista) / len(sublista) # sumamos y dividimos por la cantidad de elementos
        lista_promedios.append(promedio)
    return lista_promedios
    
    ...
    
otra verion mas corta y elegante 
def promedio_anidadas(lista_anidada)
    return[sum(sublista)/len(sublista) for sublista in lista_anidada]
    
'''