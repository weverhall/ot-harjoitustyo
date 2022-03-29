import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    kassapaate = Kassapaate()

    def setUp(self):
        self.kassapaate.kassassa_rahaa = 100000
        self.kassapaate.edulliset = 0
        self.kassapaate.maukkaat = 0

    def test_oikea_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lounaita_ei_myyty(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)