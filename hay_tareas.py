def hay_tareas(lista_tareas):
    if len(lista_tareas) == 0:
        return "No hay tareas"
    else:
        return "Hay tareas pendientes"

print(hay_tareas(["mover coche", "cambiar rueda", "pintar coche"]))
print(hay_tareas([]))
