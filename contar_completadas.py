def contar_completadas(tareas):
    contador = 0
    for tarea in tareas:
        if tarea["completada"] == True:
            contador = contador + 1
    return contador

tareas = [
    {"titulo": "lavar el auto", "completada": True},
    {"titulo": "comprar pan", "completada": False},
    {"titulo": "estudiar Python", "completada": False}
]

print(contar_completadas(tareas))
