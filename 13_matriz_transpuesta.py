# dada una matriz (listas de listas) crear una funcion que devuelve su transpuesta
def matriz_transpuesta(matriz):
    transpuesta = [] # aqui guardaremos las filas de la nueva matriz 
    
    # recorremos por columnas (usamos range() sobre el numero de columnas)
    for col in range(len(matriz[0])):
        nueva_fila = [] # esta fila se ira llenando con elementos de la columna col 
        
        # recorremos las filas 
        for fila in matriz :
            nueva_fila.append(fila[col]) # cogemos el elemento en esa columna
        transpuesta.append(nueva_fila) # agregamos la fila ya formada a la matriz 
        
    return transpuesta

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matriz_transpuesta(matriz))
