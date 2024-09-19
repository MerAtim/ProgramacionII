# Pedir numeros y guardarlos en una lista. Cuando el usuario introduzca un numero 0, nuestro programa dejaria de insertar. Mostrar los numeros ordenados de menor a mayor.

lista = []  # Inicializamos una lista vacia.

while True:
    # Solicitamos un numero al usuario
    numero = int(input("Ingrese un numero. 0 para finalizar: "))
    if numero == 0:  # Si el numero ingresado es 0, el programa debe detenerse
        break
    # Se agrega a la lista el numero ingresado por el usuario
    lista.append(numero)

lista.sort()  # Aqui ordenamos los numeros de forma ascendente.

print(f"\nLos numeros ingresados ordenados de menor a mayor son: {lista}")
