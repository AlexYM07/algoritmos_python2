# funcion para saber los pares de listas anidadas
def impares_listas_anidadas(lista_anidada):
    impares = []
    for sublistas in lista_anidada:
        sublista_impares = []
        for numero in sublistas:
            if numero % 2 != 0:
                sublista_impares.append(numero)
        impares.append(sublista_impares)
    return impares

listas = [
    [1, 2, 3],
    [4, 8],
    [9, 7, 10]
]
print(impares_listas_anidadas(listas))