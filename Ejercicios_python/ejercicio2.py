while True:
    nombre = input("¿Cuál es tu nombre? ")
    if nombre.isalpha():
        print("Hola " + nombre + "¿cómo estás?")
        break
    else:
        print("Error: Por favor introduce tu nombre (Sin numeros).")
