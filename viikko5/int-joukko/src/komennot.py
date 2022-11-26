class Kuuluu:
    def suorita(self, luku, lukujono, alkioiden_lkm):
        return luku in lukujono[:alkioiden_lkm]


class Lisaa:
    def suorita(self, luku, lukujono, indeksi):
        lukujono[indeksi] = luku


class Kasvata:
    def suorita(self, lukujono, kasvatuskoko):
        return lukujono + [0]*kasvatuskoko


class Poista:
    def suorita(self, luku, lukujono):
        siirra = False
        for (i, alkio) in enumerate(lukujono):
            if siirra:
                lukujono[i-1] = lukujono[i]
                lukujono[i] = 0
            if alkio == luku:
                lukujono[i] = 0
                siirra = True
        return siirra
