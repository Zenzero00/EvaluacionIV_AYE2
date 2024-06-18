class Pila:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return not self.elementos

    def apilar(self, item):
        self.elementos.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()

    def cima(self):
        if not self.esta_vacia():
            return self.elementos[-1]


class Cola:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return not self.elementos

    def encolar(self, item):
        self.elementos.insert(0, item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop()

    def frente(self):
        if not self.esta_vacia():
            return self.elementos[-1]
