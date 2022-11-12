import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self) -> None:
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1 or tuote_id == 2:
                return 10
            return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "jugurtti", 8)
            if tuote_id == 3:
                return Tuote(3, "hummus", 3)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called()

    def test_tilisiirtoa_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, '12345', '33333-44455', 5)

    def test_ostetaan_kaksi_eri_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("jucka", "54321")
        self.pankki_mock.tilisiirto.assert_called_with("jucka", 42, '54321', '33333-44455', 13)

    def test_ostetaan_kaksi_samaa_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("jucka", "54321")
        self.pankki_mock.tilisiirto.assert_called_with("jucka", 42, '54321', '33333-44455', 10)

    def test_ostetaan_kaksi_tuotetta_toinen_loppu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("jucka", "54321")
        self.pankki_mock.tilisiirto.assert_called_with("jucka", 42, '54321', '33333-44455', 5)

    def test_edellisen_ostoksen_tiedot_nollataan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("jucka", "54321")
        self.assertAlmostEqual(self.kauppa._ostoskori.hinta(), 5)
        self.kauppa.aloita_asiointi()
        self.assertAlmostEqual(self.kauppa._ostoskori.hinta(), 0)

    def test_uusi_viitenumero_muodostetaan_jokaiselle_maksutapahtumalle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("jucka", "54321")
        self.assertAlmostEqual(self.viitegeneraattori_mock.uusi.call_count, 1)
        self.kauppa.tilimaksu("jucka", "54321")
        self.kauppa.tilimaksu("jucka", "54321")
        self.kauppa.tilimaksu("jucka", "54321")
        self.assertAlmostEqual(self.viitegeneraattori_mock.uusi.call_count, 4)

    def test_korista_voidaan_poistaa_ostoksia(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.assertAlmostEqual(self.kauppa._ostoskori.hinta(), 5)
        self.kauppa.poista_korista(1)
        self.assertAlmostEqual(self.kauppa._ostoskori.hinta(), 0)
