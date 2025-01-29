def eliminar_duplicados(lista_palabras):
    return list(set(lista_palabras))

palabras = ["manzana", "pera", "manzana", "naranja", "pera"]
resultado = eliminar_duplicados(palabras)
print(resultado)