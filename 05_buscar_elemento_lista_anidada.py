# recibir una lista y un elemento , devolver true si esta en la lista, y false si no 

def busqueda_elemento(lista_anidada, num):
    # recorremos cada sublista
    for sublista in lista_anidada:
        # si el numero esta en esta sublista
        if num in sublista:
            return True # devolvemos True inmediatamente
    # si terminamos de recorrer todsa las sublistas y no lo encontramos
    return False
        
            
listas = [
    [2, 3, 4],
    [6, 7, 8, 9],
    [1 , 10, 22]
]
print(busqueda_elemento(listas, 10))