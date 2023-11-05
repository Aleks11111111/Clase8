
import problema1
from alumnos import alumnos

'''
Hasta ahora hemos   Seguir Escribiendo


Trabajando con variables
que    permiten alamcenar
un único valor
'''

edad = 12

altura = 1.79

nombre = "Juan"

estado = True

'''
En Python podemos
usar una variable
que almacena una
coleccion de datos
y luego accederla
usando un subincice
'''

# Lista de enteros
lista1 = [10, 5, 3, 9]

# lista de decimales
lista2 = [1.78, 2.66, 1.55, 89.4, 6.9]

# Lista de string
lista3 = ["Lunes","Martes","Miercolés"]

# Lista de elementos de distinto tipo
lista4 = ["Juan", 45, 1.92, False]

if __name__ == '__main__':

    # Cantidad de elementos de cada lista:
    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    print()
    print(lista1)
    lista1[0] = 1
    print()
    print(lista1)

    print()

    problema1.suma_5_enteros()

    print()

    alumnos()



