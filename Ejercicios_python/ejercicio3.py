try: 
    celsius = float(input("Introduce la temperatura en °C para comvertirla a °F : "))
    fahrenheit = (celsius * 9) /5 + 32
    print("Celsius: ", celsius, " a Fahrenheit es: ", fahrenheit)
except ValueError:
    print("Error: Por favor ingresar un número, no se acepta texto.")
