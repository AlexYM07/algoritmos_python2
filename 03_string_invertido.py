# funcion que recibe un string y devuelve la misma palabra pero invertida

def string_invertido(palabra):
    invertida = "" # varible donde va a estar la nueva palabra
    for i in palabra: #  recorremos cada letra de la plabra
        invertida = i + invertida # se va anadiendo cada letra pero al reves de atras pa alante
    return invertida

print(string_invertido("Hola"))
        
"""
def string_invertido_corto(palabra):
    return palabra[::-1]
    
palabra[start:stop:step] 
es la forma de hacer slicing en Python.

[::-1] significa:

start y stop se dejan vacíos → 
Python toma toda la cadena.

step = -1 → 
recorre la cadena de atrás hacia adelante.

"""