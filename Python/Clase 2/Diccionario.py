# Llave : valor  <- Un diccionario esta compuesto por estos dos datos.
# "Maradona" : 10  dict(key, value)

diccionario = {
    "IDE": "Integrated Development Enviroment",
    "POO": "Programacion orientada a Objetos",
    "SABD": "Sistema de Administracion de Base de Datos"
}

print("Estos son los elementos del diccionario: ", diccionario)

# Len muestra la cantidad de elementos que existen.
print("\nVamos a ver la longitud del diccionario: ")
print(len(diccionario))

print("\nAcceder a un elemento del diccionario: ")  # Se accede con la clave
# Nos debe mostrar el valor para la llave ingresada. Cuidar mayusculas y minusculas.
print(diccionario["IDE"])

print("\nOtra forma de acceder a los elementos es con la funcion get(): ")
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

print("\nModificamos elementos en el diccionario: ")
# Sobreescribimos el valor
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

print("\nRecorrer las claves en el diccionario: ")  # Solo muestra las llaves
for clave in diccionario:
    print(clave)

print("\nPara recorrer las claves y valores en el diccionario se necesita la funcion items(): ")
# Para mostrar clave y valor se usa items().
for clave, valor in diccionario.items():
    print(clave, valor)

print("\nPara recorrer solamente las claves en el diccionario se necesita la funcion keys(): ")
for clave in diccionario.keys():  # Para mostrar la clave se usa keys().
    print(clave)

print("\nPara recorrer solamente los valores en el diccionario se necesita la funcion values(): ")
for valor in diccionario.values():  # Para mostrar el valor se usa values().
    print(valor)

print("\nComprobamos si existe un elemento en el diccionario: ")
# Devuelve un booleano. Respetar mayus y minusculas.
print("IDE" in diccionario)
# Para verificar que no esta en el diccionario usamos NOT IN
print("UTN" not in diccionario)

print("\nAgregamos un elemento en el diccionario: ")
diccionario["PK"] = "Primary Key"  # Agregamps nueva Clave y valor.
print(diccionario)  # Nos muestra los elementos actualizados.

print("\nEliminamos un elemento del diccionario con pop(): ")
# Se eliminan Clave y Valor del argumento especificado.
diccionario.pop("SABD")
print(diccionario)  # Nos muestra los elementos actualizados.

print("\nEliminamos los elementos del diccionario: ")
diccionario.clear()  # Se eliminan Claves y Valores del diccionario
# Muestra solo las llaves vacías, es decir que el diccionario no tiene elementos.
print(diccionario)

print("\nEliminamos el diccionario con del")
del diccionario  # delete borra todo el diccionario.
