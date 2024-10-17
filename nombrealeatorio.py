import random 
import string 

def generar_nombre(nombre, longitud):
    caracteres = string.ascii_letters + string.digits
    random_part = ''.join(random.choice(caracteres)
                          for x in range(longitud))
    return print(nombre + random_part)

nombre = input("nombre: ")
randoms = ''.join(random.choice(nombre))
nombre = f'{randoms}{nombre}{randoms}'
longitud = int(input("longitud: "))
generar_nombre(nombre, longitud)