class Persona:
    def __init__(self, nombre, edad):
        """Inicializa una nueva instancia de Persona con nombre y edad."""
        self._nombre = nombre  # Almacena el nombre
        self._edad = edad      # Almacena la edad

    @property
    def nombre(self):
        """Devuelve el nombre de la persona."""
        return self._nombre  # Retorna el nombre

    @property
    def edad(self):
        """Devuelve la edad de la persona."""
        return self._edad  # Retorna la edad

    def __add__(self, other):
        """Concatena los nombres de dos personas."""
        return self._nombre + " " + other.nombre  # Retorna la concatenación de nombres

    def __sub__(self, other):
        """Resta las edades de dos personas."""
        return self._edad - other.edad  # Retorna la diferencia de edad

# Crear instancias de Persona
persona1 = Persona("Nelson", 40)  # Crea una persona llamada Nelson de 40 años
persona2 = Persona("Rios", 5)      # Crea una persona llamada Rios de 5 años

# persona1.__add__(persona2) Sintaxis interna y automatica

# Usar las operaciones definidas
print(persona1 + persona2)  # Imprime "Nelson Rios"
print(persona1 - persona2)   # Imprime 35