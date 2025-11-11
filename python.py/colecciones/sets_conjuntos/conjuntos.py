'''Crea dos conjuntos con números y muestra: unión, intersección, diferencia'''

set1 = {1, 2, 3, 4, 5, 6, 7}

set2 = {4, 5, 6, 7, 8, 9, 10}

union = set1.union(set2)

interseccion = set1.intersection(set2)

diferencia1= set1.difference(set2)
diferencia2 = set2.difference(set1)
diferencia = diferencia1.union(diferencia2)


print(f"Unión: {union} | Intersección: {interseccion} | Diferencia: {diferencia}")


