class KiviPaperiSakset:
    def pelaa(self, tuomari):

        ekan_siirto = self.hae_ekan_valinta()
        tokan_siirto = self.hae_tokan_valinta()
        self.tulosta_tietokoneen_siirto(tokan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self.hae_ekan_valinta()
            tokan_siirto = self.hae_tokan_valinta()
            self.tulosta_tietokoneen_siirto(tokan_siirto)
            self.aseta_tietokoneen_siirto(tokan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto in ["k", "p", "s"]

    def hae_ekan_valinta(self):
        pass

    def hae_tokan_valinta(self):
        pass

    def tulosta_tietokoneen_siirto(self, siirto):
        pass

    def aseta_tietokoneen_siirto(self, siirto):
        pass
