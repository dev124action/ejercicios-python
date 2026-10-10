def marcar_completada(tarea):
    tarea["completada"] = True
    return tarea

tarea = {"titulo": "comprar pan", "completada": False}
print(tarea)

tarea_actualizada = marcar_completada(tarea)
print(tarea_actualizada)
