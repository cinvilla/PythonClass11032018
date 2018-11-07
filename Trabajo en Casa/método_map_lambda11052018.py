# la expresión se ejecta y el resultado es devuelto
x = lambda a : a + 10
print(x(5))

# cualquier # de argumentos
x = lambda a,b : a * b
print(x(5,6))

# suma 3 argumentos
x = lambda a,b,c : a + b + c
print(x(5,6,7))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)  # doubles the number that you sent
print(mydoubler(11))

mydoubler = myfunc(4)
print(mydoubler(2))

# myfunc(2) = lambda a : a * 2
# mydoubler(11) = pasar el argumento dentro de esa función a la función de 2
