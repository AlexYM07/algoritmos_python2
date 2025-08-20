# dada una lista anidada, devolver una lista con el maximo de cada sublista 
def maximo_lista_anidada(lista_anidada):
        lista_maximos = [] # nueva lista para los maximos
        for sublista in lista_anidada: # recorremos primero las sublistas
            maximo = sublista[0] # el primer valor de cada sublista , de esa manera cada sublista arranca con su propio maximo y no depende de la anterior 
            for numero in sublista: # recorremos cada sublista y sus numeros
                if numero > maximo: # comparar numeros
                    maximo = numero # actualizar el valor de maximo 
            # importante la identacion aqui, porque si la ponemos al igual que la linea
            # anterior pues daria un mal resultado
            # se pone fuera del segundo for para que nos de el maximo de cada una 
            lista_maximos.append(maximo) 
    
        return lista_maximos

listas = [
    [1, 2, 3],
    [3, 4],
    [77, 45, 23, 908]
]

print(maximo_lista_anidada(listas))
