"""
Modulo que define la clase Nodo para un arbol binario.
"""


class Nodo:
    """Representa un nodo en un arbol binario."""

    def __init__(self, valor):
        """Inicializa un nodo con un valor."""
        self.__valor = valor
        self.__izquierdo = None
        self.__derecho = None

    # Getters
    def get_valor(self):
        """Retorna el valor del nodo."""
        return self.__valor

    def get_izquierdo(self):
        """Retorna el hijo izquierdo."""
        return self.__izquierdo

    def get_derecho(self):
        """Retorna el hijo derecho."""
        return self.__derecho

    # Setters
    def set_valor(self, valor):
        """Establece un nuevo valor para el nodo."""
        self.__valor = valor

    def set_izquierdo(self, nodo):
        """Establece el hijo izquierdo."""
        self.__izquierdo = nodo

    def set_derecho(self, nodo):
        """Establece el hijo derecho."""
        self.__derecho = nodo