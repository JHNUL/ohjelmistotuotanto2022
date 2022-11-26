from enums import Komento


class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.komennot = []

    def _lisaa_muistiin(self, komento):
        if len(self.komennot) > 100:
            self.komennot = self.komennot[1:]
        self.komennot.append(komento)

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo
        self._lisaa_muistiin(Komento.EROTUS)

    def plus(self, arvo):
        self.tulos = self.tulos + arvo
        self._lisaa_muistiin(Komento.SUMMA)

    def nollaa(self):
        self.tulos = 0
        self._lisaa_muistiin(Komento.NOLLAUS)

    def hae_edellinen_komento(self):
        if len(self.komennot) > 0:
            return self.komennot.pop()
        return None

    def aseta_arvo(self, arvo):
        self.tulos = arvo
