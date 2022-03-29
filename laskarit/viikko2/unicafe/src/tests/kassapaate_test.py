import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassassa_rahaa = Kassapaate.kassassa_rahaa()
        self.edulliset = Kassapaate.edulliset()
        self.maukkaat = Kassapaate.maukkaat()

    def test_oikea_rahamaara(self):
        self.assertEqual(self.kassassa_rahaa, 100000)

    def test_lounaita_ei_myyty(self):
        self.assertEqual(self.edulliset, 0)
        self.assertEqual(self.maukkaat, 0)