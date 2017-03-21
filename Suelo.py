
class Suelo:
    lista = []

    def add(self, baldosa):
        self.lista.append(baldosa)

    def dibuja(self):
        for baldosa in self.lista:
            baldosa.dibuja()

    def actualiza(self, t):
        for baldosa in self.lista:
            baldosa.actualiza(t)

    def getLista(self):
        return self.lista
