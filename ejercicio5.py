def frecuencia_palabras():
    frase="Puta betis balompie"
    palabras=frase.split()
    frecuencia={}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra]+=1
        else:
            frecuencia[palabra]=1

    return frecuencia

frecuencia_palabras()
print(frecuencia_palabras())