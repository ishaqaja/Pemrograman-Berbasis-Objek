# test_diskon.py
import unittest
from diskon_service import DiskonCalculator


class TestDiskonCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = DiskonCalculator()

    def test_diskon_standar_10_persen(self):
        """Diskon 10% dari 1000 harus menghasilkan 900"""
        hasil = self.calc.hitung_diskon(1000, 10)
        self.assertEqual(hasil, 900.0)

    def test_diskon_nol(self):
        """Diskon 0% tidak mengubah harga"""
        hasil = self.calc.hitung_diskon(500, 0)
        self.assertEqual(hasil, 500.0)

    def test_diskon_batas_atas(self):
        """Diskon 100% menghasilkan harga 0"""
        hasil = self.calc.hitung_diskon(750, 100)
        self.assertEqual(hasil, 0.0)

    def test_input_negatif(self):
        """Diskon negatif tidak boleh menurunkan harga"""
        hasil = self.calc.hitung_diskon(500, -5)
        self.assertGreaterEqual(hasil, 500)


if __name__ == '__main__':
    unittest.main()
