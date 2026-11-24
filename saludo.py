def saludar(nombre_completo):
    if not nombre_completo:
        return "Hola, invitado"
    return f"Hola {nombre_completo}"

print(saludar("GitHub"))