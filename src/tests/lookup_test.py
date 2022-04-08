import unittest
from services.lookup_service import NetworkLookup

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa")