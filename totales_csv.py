import csv

with open("notas.csv") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        total = int(fila["nota1"]) + int(fila["nota2"]) + int(fila["nota3"])
        print(fila["nombre"] + " Total: " + str(total))
