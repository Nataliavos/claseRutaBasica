
# definimos la función
def saludar():
    print("Hola mundo")

# llamamos la función para que se ejecute
saludar()


# mostrar bienvenida
def mostrar_bienvenida():
    print("Hola coder, bienvenido al clan Hamilton!")

mostrar_bienvenida()

# === Función con parámetros ===
def saludar_estudiante(nombre):
    print("Hola", nombre, "Bienvenido")

saludar_estudiante("Andres")

# función que imprima nombre y edad
def mostrar_datos(nombre, edad):
    print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

mostrar_datos("Natalia", 27)

# sumar
def sumar(a, b):
    resultado = a + b
    # return devuelve el valor de la operación
    return resultado

total = sumar(5, 5)
print("La suma es: ", total)

# multiplicar
def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

total = multiplicar(8, 10)
print(f"El resultado es: {total}")

