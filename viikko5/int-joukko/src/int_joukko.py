from komentotehdas import Komentotehdas, Komento


class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = [0] * kapasiteetti
        self.alkioiden_lkm = 0
        self.komennot = {
            Komento.KUULUU: Komentotehdas.luo(Komento.KUULUU).suorita,
            Komento.KASVATA: Komentotehdas.luo(Komento.KASVATA).suorita,
            Komento.LISAA: Komentotehdas.luo(Komento.LISAA).suorita,
            Komento.POISTA: Komentotehdas.luo(Komento.POISTA).suorita,
        }

    def kuuluu(self, luku):
        return self.komennot[Komento.KUULUU](luku, self.lukujono, self.alkioiden_lkm)

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False

        self.komennot[Komento.LISAA](
            luku, self.lukujono, self.alkioiden_lkm)

        self.alkioiden_lkm += 1
        if self.alkioiden_lkm == len(self.lukujono):
            self.lukujono = self.komennot[Komento.KASVATA](
                self.lukujono, self.kasvatuskoko)

        return True

    def poista(self, luku):
        poistettiin = self.komennot[Komento.POISTA](luku, self.lukujono)
        if poistettiin:
            self.alkioiden_lkm -= 1
        return poistettiin

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for luku in a_taulu:
            x.lisaa(luku)
        for luku in b_taulu:
            x.lisaa(luku)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            if luku in b_taulu:
                y.lisaa(luku)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            if luku not in b_taulu:
                z.lisaa(luku)

        return z

    def __str__(self):
        return f"{str(self.lukujono[:self.alkioiden_lkm]).replace('[', '{').replace(']', '}')}"
