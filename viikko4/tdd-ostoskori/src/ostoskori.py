from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = {}

    def tavaroita_korissa(self):
        c = 0
        for kilke in self._ostokset.values():
            c += kilke.lukumaara()
        return c

    def hinta(self):
        p = 0
        for kilke in self._ostokset.values():
            p += kilke.hinta()
        return p

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi() in self._ostokset:
            self._ostokset[lisattava.nimi()].muuta_lukumaaraa(1)
        else:
            self._ostokset[lisattava.nimi()] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        if poistettava.nimi() in self._ostokset:
            self._ostokset[poistettava.nimi()].muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self._ostokset.values())
