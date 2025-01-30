def diccionario(texto):
    vocales = "aeiouAEIOU"
    contador_vocales= 0
    contador_consonantes = 0
    for letra in texto:
        if letra in vocales:
            contador_vocales += 1
        else:
            contador_consonantes += 1
    return {"vocales": contador_vocales, "consonantes": contador_consonantes}

print(diccionario("Hola Mundo"))
