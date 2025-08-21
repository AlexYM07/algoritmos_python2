def sumas_impares_pares(lista_anidada):
    lista_final = [] # aqui guardamos los resultados de cada sublista
    
    for sublista in lista_anidada:
        suma_pares = 0
        suma_impares = 0
        
        for numero in sublista:
            if numero % 2 == 0:
                suma_pares += numero
            else:
                suma_impares += numero
        
        #aqui unimos las dos sumas en un diccionario
        union = {"pares": suma_pares, "impares": suma_impares}
        
        # lo agregamos a la lista de resultados 
        lista_final.append(union)
        
    return lista_final
    
listas = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]

print(sumas_impares_pares(listas))
