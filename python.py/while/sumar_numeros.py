'''Lista con 10 nombres, la ejecucion se para cuando llegue a 10 nombres o cuando el usuario ingrese "andres"'''

nombres = []
nombre = ""

while not nombre == "andres":
    nombre = input("Ingrese un nombre: ").lower()
    nombres.append(nombre)
    if len(nombres) == 10:
        break

print(nombres)

# while not ("andres" in nombres or len(nombres) == 10)