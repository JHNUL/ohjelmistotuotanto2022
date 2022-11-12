KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self.validoi_arvo(kapasiteetti, 'kapasiteetti', KAPASITEETTI)
        self.kasvatuskoko = self.validoi_arvo(kasvatuskoko, 'kasvatuskoko', OLETUSKASVATUS)
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def validoi_arvo(self, arg, nimi, default_arvo):
        if arg is None:
            return default_arvo

        if not isinstance(arg, int) or arg < 0:
            raise Exception(f"Epäkelpo {nimi}: {arg}")

        return arg

    def kasvata_lukujonon_kokoa(self):
        self.lukujono += [0] * self.kasvatuskoko

    def kuuluu(self, luku):
        return luku in self.lukujono

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.lukujono):
                self.kasvata_lukujonon_kokoa()

            return True

        return False

    def poista(self, luku):
        loytyi = False
        for i in range(0, self.alkioiden_lkm):
            if luku == self.lukujono[i]:
                self.lukujono[i] = 0
                loytyi = True
            if loytyi and i < self.alkioiden_lkm - 1:
                self.lukujono[i] = self.lukujono[i+1]
                self.lukujono[i+1] = 0
        if loytyi:
            self.alkioiden_lkm -= 1
        return loytyi

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        yhdiste_joukko = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for a_luku in a_taulu:
            yhdiste_joukko.lisaa(a_luku)

        for b_luku in b_taulu:
            yhdiste_joukko.lisaa(b_luku)

        return yhdiste_joukko

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        leikkaus_joukko = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for luku in a_taulu:
            if luku in b_taulu:
                leikkaus_joukko.lisaa(luku)

        return leikkaus_joukko

    @staticmethod
    def erotus(joukko_a, joukko_b):
        erotus_joukko = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for luku in a_taulu:
            if luku not in b_taulu:
                erotus_joukko.lisaa(luku)

        return erotus_joukko

    def __str__(self):
        alkiot = ', '.join(list(map(lambda i: str(i), self.lukujono[:self.alkioiden_lkm])))
        return f"{{{alkiot}}}"
