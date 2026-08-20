"""
Modulo que define la clase Arbol binario de busqueda.
"""

from Nodo import Nodo


class Arbol:
    """Arbol binario de busqueda (ABB).
    Regla: menores a la izquierda, mayores a la derecha.
    """

    def __init__(self):
        """Inicializa un arbol vacio."""
        self.__raiz = None

    # Getters
    def get_raiz(self):
        """Retorna la raiz del arbol."""
        return self.__raiz

    # Setters
    def set_raiz(self, nodo):
        """Establece la raiz del arbol."""
        self.__raiz = nodo

    # Insertar (mantiene el orden)
    def insertar(self, valor):
        """Inserta un valor en el arbol (menores a izquierda, mayores a derecha)."""
        nuevo = Nodo(valor)

        if self.__raiz is None:
            self.__raiz = nuevo
            return

        actual = self.__raiz
        while True:
            # Si es menor, va a la izquierda
            if valor < actual.get_valor():
                if actual.get_izquierdo() is None:
                    actual.set_izquierdo(nuevo)
                    break
                actual = actual.get_izquierdo()
            # Si es mayor, va a la derecha
            else:
                if actual.get_derecho() is None:
                    actual.set_derecho(nuevo)
                    break
                actual = actual.get_derecho()

    # Mostrar arbol
    def mostrar(self, nodo=None, nivel=0):
        """Muestra el arbol de forma visual."""
        if nodo is None:
            nodo = self.__raiz

        if nodo is None:
            print("Arbol vacio")
            return

        espacio = "  " * nivel

        if nivel == 0:
            print(f"{espacio}-> {nodo.get_valor()} (raiz)")
        else:
            print(f"{espacio}-> {nodo.get_valor()}")

        if nodo.get_izquierdo() is not None:
            self.mostrar(nodo.get_izquierdo(), nivel + 1)
        else:
            print(f"{espacio}   -> None")

        if nodo.get_derecho() is not None:
            self.mostrar(nodo.get_derecho(), nivel + 1)
        else:
            print(f"{espacio}   -> None")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================
if __name__ == "__main__":
    # Crear arbol
    arbol = Arbol()

    # Insertar valores (se ordenan solos)
    print("Insertando valores: 50, 30, 70, 20, 40, 60, 80")
    valores = [50, 30, 70, 20, 40, 60, 80]
    for v in valores:
        arbol.insertar(v)

    # Mostrar arbol
    print("\nEstructura del arbol:")
    arbol.mostrar()

