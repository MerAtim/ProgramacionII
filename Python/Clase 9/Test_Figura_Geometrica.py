from Cuadrado import Cuadrado # del archivo Cuadrado importa la clase Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, "Azul") # Instanciamos un nuevo objeto Cuadrado
print(cuadrado1.ancho) # Mostramos el ancho
print(cuadrado1.alto) # Mostramos el alto
print(f"Calculo del area del cuadrado: {cuadrado1.calcular_area()}")

# MRO Method Resolution Order
print(Cuadrado.mro())
print(cuadrado1)

# Instanciamos un objeto Rectángulo:
rectangulo1 = Rectangulo(3, 8, "Verde")
print(Rectangulo.mro())
print(rectangulo1)