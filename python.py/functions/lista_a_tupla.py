'''Convierte una lista de números a tupla y muestra el primer y último elemento'''

numeros = [500, 45, 88, 90]

# la función tuple(list) convierte una tupla en una lista
tupla = tuple(numeros)
# list[0] muestra el valor en la primera posición de la lista y list[-1] muestra el último
print(f"El primer número de la lista es: {tupla[0]} y el último es: {tupla[-1]}")