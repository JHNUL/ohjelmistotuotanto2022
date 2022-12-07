from kps import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def hae_ekan_valinta(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def hae_tokan_valinta(self):
        return input("Toisen pelaajan siirto: ")
