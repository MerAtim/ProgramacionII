# Los sets no tienen indice, por lo mismo no son ordenados. Pero nos sirve para listas donde se repiten los elementos ya que muestra solo 1 si estan repetidos.

print("Creamos un set llamado Planeta, que contiene los siguientes elementos: ")
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

print("\nVer la cantidad de elementos en el set: ")
print(len(planetas))  # Vemos la dimension del set. La cantidad de elementos.

# Ver si un elemento existe dentro de set.
print("\nVer si un elemento existe dentro de set: ")
# Ser cuidadosos y respetar mayusculas o minusculas para que coincida.
print("Mercurio" not in planetas)

print("\nAgregamos un nuevo elemento al set: ")
# con add agregamos elementos, no se agregan duplicados. Solamente una vez se muestran.
planetas.add("Tierra")
print(planetas)

# Nos puede dar error si el elemento no existe.
print("\nEliminamos un elemento del set: ")
planetas.remove("Jupiter")
print(planetas)
# Discard es descartar,a diferencia de remove, no rompe la ejecucion si ingresamos mal el elemento.
planetas.discard("Tierra")

# Nos puede dar error si el elemento no existe.
print("\nPodemos organizar elementos del set: ")
planetasOrdenados = sorted(planetas)
print(planetasOrdenados)

# Nos puede dar error si el elemento no existe.
print("\nPara eliminar los elementos del set: ")
planetas.clear()
print(planetas)  # muestra el conjunto vacío.

# Nos puede dar error si el elemento no existe.
print("\nUsamos DEL para eliminar el set: ")
del planetas
print(planetas)  # Nos va a mostrar error ya que eliminó el conjunto.
