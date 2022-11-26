class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.tulokset = []

    def suorita(self):
        self.tulokset.append(self.sovelluslogiikka.tulos)
        self.sovelluslogiikka.plus(self.lue_syote())

    def kumoa(self):
        if len(self.tulokset) > 0:
            self.sovelluslogiikka.aseta_arvo(self.tulokset.pop())


class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.tulokset = []

    def suorita(self):
        self.tulokset.append(self.sovelluslogiikka.tulos)
        self.sovelluslogiikka.miinus(self.lue_syote())

    def kumoa(self):
        if len(self.tulokset) > 0:
            self.sovelluslogiikka.aseta_arvo(self.tulokset.pop())


class Nollaus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.tulokset = []

    def suorita(self):
        self.tulokset.append(self.sovelluslogiikka.tulos)
        self.sovelluslogiikka.nollaa()

    def kumoa(self):
        if len(self.tulokset) > 0:
            self.sovelluslogiikka.aseta_arvo(self.tulokset.pop())
