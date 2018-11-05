## Ejemplo tomado de https://www.python-course.eu/python3_lambda.php

def fahrenheit(T): # acá estamos definiendo la función farenheit con argumento T, este argumento es básicamente una variable que se igualará al varlor que se le dé a T dentro del código.
    return ((float(9) / 5) * T + 32) # Este es el cuerpo de la función lo que nos va a dar de vuelta.


def celsius(T): # acá estamos definiendo la función celsius
    return (float(5) / 9) * (T - 32)


temperatures = (36.5, 37, 37.5, 38, 39) # esta tupla va a contener los elementos que pasaremos a través del function object en map
F = map(fahrenheit, temperatures)
C = map(celsius, F)

temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures)) # A los elementos en tempetures se les aplicará la función fahrenhet
# en la primera vuelta ((float(9) / 5) * 36.5 + 32)
# en la segunda vuelta ((float(9) / 5) * 37 + 32)
# y así sucesivamente hasta darle la vuelta a la secuencia de números.
# el resultado será pasado a la función para definir el output como tipo lista

temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit)) # A la lista resultante de la ecuación anterior se le aplicará la function celsius gracias a map para obtener los valores
print(temperatures_in_Fahrenheit)
print(temperatures_in_Celsius)

