from kps import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):

    def __init__(self, tuomari, tekoaly):
        super().__init__(tuomari)
        self.tekoaly = tekoaly

    def _tokan_siirto(self, ekan_siirto=None):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
