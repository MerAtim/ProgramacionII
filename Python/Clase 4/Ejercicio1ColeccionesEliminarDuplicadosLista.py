# Escriba un programa donde cree una lista y que a continuación
# elimine los elementos repetidos. Por último mostrar la lista.

# Lista con elementos repetidos.
conRepetidos = [1, 1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 8, 9, 9, 9, 9]

# Convertimos la lista a conjunto para eliminar los repetidos.
sinRepetidos = list(set(conRepetidos))

print(f"La lista con datos repetidos se ve asi: {conRepetidos}")
print(f"Asi queda la lista con elementos sin repetir: {sinRepetidos}")
