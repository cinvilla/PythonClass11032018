## Ejemplo tomado de https://www.python-course.eu/python3_lambda.php

C = [39.2, 36.5, 37.3, 38, 37.8] # lista de números en secuencia a los que se les aplicará la función en map
F = list(map(lambda x: (float(9) / 5) * x + 32, C)) # En lambda se define lo que le hará la función a los elementos con una expresión aritmética
print(F) # En la variable C, se le aplicará la función lambda a cada uno de sus elementos
C = list(map(lambda x: (float(5) / 9) * (x - 32), F))
print(C)

