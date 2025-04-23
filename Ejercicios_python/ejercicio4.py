try:
    base = float(input("Ingresa la base del rectangulo: "))
    altura = float(input("Ingresa la altura del rectangulo: "))
    area = base * altura
    print("El área del rectángulo es:", area, " metros cuadrados")
except ValueError:
    print("Error: Debes ingresar un valor numerico, no se acepta texto.")