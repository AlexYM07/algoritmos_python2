# resta de matrices
def resta_matrices(matriz_a, matriz_b):
    if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
        return "No se pueden restar: dimensiones diferentes"
    
    resultado = []
    
    for i in range(len(matriz_a)):
        fila_resultado = []
        for j in range(len(matriz_a[0])):
            resta = matriz_a[i][j] - matriz_b[i][j]
            fila_resultado.append(resta)
        resultado.append(fila_resultado)
    
    return resultado

matriz_A = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_B = [
    [7, 8, 9],
    [10, 11, 12]
]

print(resta_matrices(matriz_A, matriz_B))