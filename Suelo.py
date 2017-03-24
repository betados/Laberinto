
class Suelo:
    lista = []

    def add(self, baldosa):
        self.lista.append(baldosa)

    def dibuja(self,debugueandoEnOficina):
        for baldosa in self.lista:
            baldosa.dibuja(debugueandoEnOficina)

    def getLista(self):
        return self.lista

    def quitaParedes(self, listacamino):
        for baldosa in self.lista:
            for camino in listacamino:
                if camino == baldosa.getPos():
                    print("La baldosa ",baldosa.getPos()," tiene un camino que parte de ella")


