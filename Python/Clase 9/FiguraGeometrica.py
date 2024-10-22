class FiguraGeometrica:
    def __init__(self, ancho, alto):
        # Inicializa el ancho y alto de la figura
        self._ancho = ancho  # Atributo privado para el ancho
        self._alto = alto    # Atributo privado para el alto

    @property
    def ancho(self):
        # Getter para el ancho
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        # Setter para el ancho
        self._ancho = value

    @property
    def alto(self):
        # Getter para el alto
        return self._alto

    @alto.setter
    def alto(self, value):
        # Setter para el alto
        self._alto = value

    def __str__(self):
        # Devuelve una representación en forma de cadena de la figura
        return f'\nFiguraGeometrica de {self.ancho} de ancho x {self.alto} de alto.'
