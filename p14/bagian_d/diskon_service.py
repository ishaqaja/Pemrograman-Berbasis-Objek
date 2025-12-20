# diskon_service.py
import pdb

"""
#code awal bug

class DiskonCalculator:
    #Menghitung harga akhir setelah diskon dan PPN.

    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        pdb.set_trace()

        # Hitung diskon
        jumlah_diskon = harga_awal * persentase_diskon / 100
        harga_setelah_diskon = harga_awal - jumlah_diskon

        # BUG: PPN 10% dihitung dua kali
        ppn = harga_setelah_diskon * 0.10
        harga_setelah_ppn = harga_setelah_diskon + ppn
        harga_setelah_ppn = harga_setelah_ppn + ppn  # BUG DI SINI

        return harga_setelah_ppn
    """

#code yang sudah di perbaiki
class DiskonCalculator:
    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        jumlah_diskon = harga_awal * persentase_diskon / 100
        harga_akhir = harga_awal - jumlah_diskon
        return harga_akhir

