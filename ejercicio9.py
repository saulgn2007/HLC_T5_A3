def calcular_promedio(estudiantes):
    total_notas = sum(estudiantes.values())
    promedio= total_notas/len(estudiantes)
    
    mejor_estudiante = max(estudiantes, key=estudiantes.get)    
    
    return "El promedio es: " ,promedio, ". Mejor estudiante " , mejor_estudiante , "con nota: ", estudiantes[mejor_estudiante]

print (calcular_promedio({"Andres": 4.5, "Juan": 3.5, "Maria": 4.0, "Pedro": 3.0}))