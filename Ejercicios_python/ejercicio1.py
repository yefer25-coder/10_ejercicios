try:
    print("Vamos a realizar una suma")
    num1 =int(input("Ingresa el primer valor: "))
    num2 =int(input("Ingresa el segundo valor: "))
    suma = num1 + num2
    print("La suma de", num1, "y", num2, "es:", suma)
except ValueError:
    print("Error: Debes ingresar un número entero, no se acepta texto.")