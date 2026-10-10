def clasificar_edad(edad):
    if edad < 13:
        return "Niño"
    elif edad >= 13 and edad <= 17:
        return "Adolescente"
    else:
        return "Adulto"

print(clasificar_edad(8))
print(clasificar_edad(15))
print(clasificar_edad(30))
