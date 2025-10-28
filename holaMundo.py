
#Imprimir nombre, edad y si es mayor o menor de edad con datos quemados
nombre = "Natalia"
edad = 27

if edad >= 18:
    estado = "soy mayor de edad"
else :
    estado = "soy menor de edad"


print (f"Mi nombre es: {nombre}")
print (f"Tengo {edad} años, ", estado)


#Imprimir nombre, edad y si es mayor o menor de edad, ingresando los datos por teclado
print ("Ingrese su nombre")
nombre = input()
print ("Ingrese su edad")
edad = int (input())


if edad >= 18:
    estado = "soy mayor de edad"
else :
    estado = "soy menor de edad"

print (f"Su nombre es {nombre} y su edad es {edad}, usted es {estado}")



#otra forma (mejor)

nombre = input("Ingrese su nombre")
edad = int(input("Ingrese la edad"))

print(f"Mi nombre es: {nombre}")
print(f"Mi edad es: {edad}")

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")