def calcular_promedio(nombre, nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    total = nota1 + nota2 + nota3
    if promedio >= 60:
        return nombre + " Total: " + str(total) + " Promedio: " + str(promedio) + " Aprobado"
    else:
        return nombre + " Total: " + str(total) + " Promedio: " + str(promedio) + " Desaprobado"

print(calcular_promedio("Juan", 70, 80, 90))
print(calcular_promedio("Ana", 40, 50, 60))
