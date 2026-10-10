def describir_tarea(lavado):
    if lavado["completada"] == True:
        return "La tarea " + lavado["titulo"] + " está completada"
    else:
        return "La tarea " + lavado["titulo"] + " está pendiente"

tarea1 = {"titulo": "lavar el auto", "completada": True}
tarea2 = {"titulo": "comprar pan", "completada": False}

print(describir_tarea(tarea1))
print(describir_tarea(tarea2))
