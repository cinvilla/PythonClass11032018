# PROGRAMA CALCULADORA SIMPLE, TAREA by Cinthya Villalobos Rojas
def menu(): # Definición de método menú, presenta el menú para la selección de la operación a realizar
    return """S - Suma
R - Resta
M - Multiplicación
D - División
E - Exit """

# Definición método BIENVENIDA al programa
def bienvenida():
    print('*********************************************'
          '¡Bienvenido al programa de operaciones simples!'
    ' Indique qué operación matemática desea utilizar:'
          '*********************************************')
    print()

# Definición de los métodos para las OPERACIONES MATEMÁTICAS, devuelve el RESULTADO de la operación matemática
# en donde los valores ingresados por el usuario y serán dispuestos como parámetros dentro del método.
suma = lambda n1, n2 : n1 + n2
resta = lambda n1,n2 : n1 - n2
multiplicacion = lambda n1,n2 : n1 * n2
division = lambda n1,n2: n1 // n2

#Cuerpo del Programa
inicio = 0
while inicio == 0:
    bienvenida()
    print(menu())
    print()
    print('Ingrese su selección:')
    seleccion_user = input().upper() # para tomar el input del usuario y pasarlo a mayúscula para que siga en
    # el bucle del if statement, ya que si le ponía 'S' or 's' tomaba cualquier letra y continuaba el bucle
    # por lo que tuve que recurrir a esta utilidad para pasar el input a mayúscula y entrara aún cuando el usuario
    # ingrese una minúscula.

# OPERACIÓN MATEMÁTICA SUMA
    if seleccion_user == 'S':
        print('Ha elegido la operación de SUMA')
        try:
            x = int(input('Ingrese un número a sumar'))
            y = int(input('Ingrese un número a sumar'))
        except ValueError:
            print()
            print('Ha ingresado una LETRA no un número')
            print('Volvamos a empezar')
            print()
        else:
            print()
            print(f'El RESULTADO de la suma es:{suma(x,y)}')
            print()
            pass

# OPERACIÓN MATEMÁTICA RESTA
    if seleccion_user == 'R':
        print('Ha elegido la operación de RESTA')
        try:
            x = int(input('Ingrese un número a restar'))
            y = int(input('Ingrese un número a restar'))
        except ValueError:
            print()
            print('Ha ingresado una LETRA no un número')
            print('Volvamos a empezar')
            print()
        else:
            print()
            print(f'El RESULTADO de la resta es: {resta(x,y)}')

# OPERACIÓN MATEMÁTICA MULTIPLICACIÓN
    if seleccion_user == 'M':
        print('Ha elegido la operación MULTIPLICACIÓN')
        try:
            x = int(input('Ingrese un número a multiplicar'))
            y = int(input('Ingrese un número a multiplicar'))
        except ValueError:
            print()
            print('Ha ingresado una LETRA no un número')
            print('Volvamos a empezar')
            print()
        else:
            print()
            print(f'El RESULTADO de la multiplicación es: {multiplicacion(x,y)}')

# OPERACIÓN MATEMÁTICA DIVISIÓN
    if seleccion_user == 'D':
        print('Ha elegido la operación DIVISIÓN')
        try:
            x = int(input('Ingrese un número a dividir'))
            y = int(input('Ingrese un número a dividir'))
        except ValueError:
            print()
            print('Ha ingresado una LETRA no un número')
            print('Volvamos a empezar')
            print()
        else:
            print()
            print(division(x, y))

# OPERACIÓN SALIR DEL PROGRAMA
    if seleccion_user == 'E':
        print('Gracias por usar nuestra calculadora, ¡Hasta pronto!')
        inicio += 1