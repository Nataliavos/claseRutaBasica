# par o impar


def tipo_num(a):
    
    if a % 2 == 0:
        tipo = "par"
        return tipo
    else:
        tipo = "impar"
        return tipo


num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
tipo1 = tipo_num(num1)
tipo2 = tipo_num(num2)
print(f"El número {num1} es {tipo1}")
print(f"El número {num2} es {tipo2}")