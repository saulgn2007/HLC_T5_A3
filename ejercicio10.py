def eliminar_numeros_pares(numeros):
    for i in numeros:
        if i % 2 == 0:
            numeros.remove(i)
    return numeros
print (eliminar_numeros_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))