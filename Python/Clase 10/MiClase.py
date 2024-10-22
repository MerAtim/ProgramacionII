class MiClase:
    # Variable de clase: Este atributo dará a cada objeto el mismo valor
    variable_clase = "Esta es la variable de clase" # Es una variable que pertenece a la clase en sí, no a los objetos individuales. Todos los objetos de MiClase compartirán el mismo valor para esta variable.
    
    def __init__(self, variable_instancia): # La variable de instancia da diferentes valores. Es un parámetro que se pasa al crear un objeto.
        self.variable_instancia = variable_instancia # Cada objeto puede tener un valor diferente para esta variable, ya que se almacena en self.variable_instancia, que es única para cada objeto.
        
print(MiClase.variable_clase) # Como es una variable de clase, muestra: "Esta es la variable de clase".
miClase = MiClase("Esta es una variable de instancia") # Pasamos el texto "Esta es una variable de instancia" como argumento. Esto asigna ese valor a self.variable_instancia para ese objeto.
print(miClase.variable_instancia) # Imprime el valor de variable_instancia para miClase, que será: "Esta es una variable de instancia".
print(miClase.variable_clase) # Aunque variable_clase es una variable de clase, se puede acceder a ella desde el objeto miClase. Imprime: "Esta es la variable de clase".

miClase2 = MiClase("Esta es otra prueba de variable de instancia") # Pasamos un valor diferente para variable_instancia. Este valor será: "Esta es otra prueba de variable de instancia".
print(miClase2.variable_instancia) # Imprime el valor de variable_instancia para miClase2, que será: "Esta es otra prueba de variable de instancia".
print(miClase2.variable_clase) # Al igual que antes, imprime la variable de clase desde miClase2, que seguirá siendo: "Esta es la variable de clase"