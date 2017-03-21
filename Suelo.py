
class Suelo:
    lista = []

    def add(self, baldosa):
        self.lista.append(baldosa)

    def dibuja(self):
        for baldosa in self.lista:
            baldosa.dibuja()

    def getLista(self):
        return self.lista
