import csv

with open("notas.csv") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila)
