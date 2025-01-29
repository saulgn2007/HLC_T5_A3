def palabras_a_longitudes(lista_palabras):
    diccionario = {palabra: len(palabra) for palabra in lista_palabras}
    return diccionario

lista = ["gato", "perro", "elefante", "Andres"]
resultado = palabras_a_longitudes(lista)
print(resultado)