from kps import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self, tuomari, tekoalyparannettu):
        super().__init__(tuomari)
        self.tekoaly = tekoalyparannettu

    def _tokan_siirto(self, ekan_siirto=None):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        if ekan_siirto is not None:
            self.tekoaly.aseta_siirto(ekan_siirto)
        return siirto
