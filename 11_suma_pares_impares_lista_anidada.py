# dada una lista de numeros, crear una funcion que devuelva, para cada sublista, 
# la suma de los numeros pares y la suma de los numeros impares
def sumas_pares_impares(lista_anidada):
    resultado = []  # Lista principal donde guardaremos los resultados por sublista
    
    for sublista in lista_anidada:  # Recorremos cada sublista
        suma_pares = 0   # Inicializamos la suma de pares de esta sublista
        suma_impares = 0 # Inicializamos la suma de impares de esta sublista
        
        for numero in sublista:  # Recorremos cada número de la sublista
            if numero % 2 == 0:   # Si el número es par
                suma_pares += numero
            else:                 # Si el número es impar
                suma_impares += numero
        
        # Una vez que terminamos la sublista, guardamos los resultados
        resultado.append({"pares": suma_pares, "impares": suma_impares})
    
    return resultado  # Devolvemos la lista completa

listas = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]

print(sumas_pares_impares(listas))