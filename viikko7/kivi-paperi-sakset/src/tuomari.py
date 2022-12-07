
# Luokka pitää kirjaa ensimmäisen ja toisen pelaajan pisteistä sekä tasapelien määrästä.
class Tuomari:
    def __init__(self):
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def kirjaa_siirto(self, ekan_siirto, tokan_siirto):
        voitokkaat = {"k": "s", "s": "p", "p": "k"}
        self.ekan_pisteet += int(voitokkaat[ekan_siirto] == tokan_siirto)
        self.tokan_pisteet += int(voitokkaat[tokan_siirto] == ekan_siirto)
        self.tasapelit += int(tokan_siirto == ekan_siirto)

    def __str__(self):
        return f"Pelitilanne: {self.ekan_pisteet} - {self.tokan_pisteet}\nTasapelit: {self.tasapelit}"
