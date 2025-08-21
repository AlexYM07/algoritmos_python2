# sumar dos matrices del mismo tamano 

# funcion que suma dos matrices
def sumar_matrices(A, B):
    # primero verificamos que tengan las mismas dimensiones 
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "No se pueden sumar: dimensiones diferentes"
    
    resultado = [] # Aqui guardaremos la matriz resultante
    
    # Recorremos las filas 
    for i in range(len(A)):
        fila_resultado = [] # Lista temporal para la fila resultante
        # recorremos las columnas 
        for j in range(len(A[0])):
            suma = A[i][j] + B[i][j] # sumamos elemento por elemento
            fila_resultado.append(suma) # anadimos el resultado a la fila 
        resultado.append(fila_resultado) # anadimos la fila completa a la matriz 
    
    return resultado 

matriz_A = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_B = [
    [7, 8, 9],
    [10, 11, 12]
]

print(sumar_matrices(matriz_A, matriz_B))