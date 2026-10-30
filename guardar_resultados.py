import csv

with open("notas.csv") as entrada, open("resultados.csv", "w", newline="") as salida:
    lector = csv.DictReader(entrada)
    escritor = csv.writer(salida)
    escritor.writerow(["nombre", "total", "promedio", "resultado"])
    for fila in lector:
        total = int(fila["nota1"]) + int(fila["nota2"]) + int(fila["nota3"])
        promedio = total / 3
        if promedio >= 60:
            resultado = "Aprobado"
        else:
            resultado = "Desaprobado"
        escritor.writerow([fila["nombre"], total, promedio, resultado])
