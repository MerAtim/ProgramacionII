# Usamos el metodo pilas con listas.
pila = [1, 2, 3]

print("Agregamos elementos a la lista apilando elementos al final: ")
pila.append(4)  # append() solo agrega un elemento a la vez.
pila.append(5)
print(pila)

print("\nEliminamos elementos de la lista desde el final: ")
# La funcion pop() elimina el ultimo elemento de la lista.
elementoBorrado = pila.pop()
print(f"Sacamos el elemento {elementoBorrado} de la lista.")
print(f"La lista ahora queda asi: {pila}")
