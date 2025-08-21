def tranpuesta(matriz):
    tranpuesta = []
    for col in range(len(matriz[0])):
        nueva_fila = []
        for fila in matriz:
            nueva_fila.append(fila[col])
        tranpuesta.append(nueva_fila)
    return tranpuesta

matriz = [
    [2, 4],
    [6, 8],
    [10, 12]
]

print(tranpuesta(matriz))