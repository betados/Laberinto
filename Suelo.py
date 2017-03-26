
class Suelo:
	lista = []

	def add(self, baldosa):
		self.lista.append(baldosa)

	def dibuja(self,debugueandoEnOficina):
		for baldosa in self.lista:
			baldosa.dibuja(debugueandoEnOficina)

	def getListaBaldosas(self):
		return self.lista

	def quitaParedes(self, listaCamino):
		for baldosa in self.lista:
			baldosa.quitaPared(listaCamino)
