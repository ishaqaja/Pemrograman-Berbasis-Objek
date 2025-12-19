# models/inventaris.py
import math

class Inventaris:
    def __init__(self):
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)

    def tampilkan_produk(self):
        print("\n=== Daftar Produk di Minimarket ===")
        for p in self.daftar_produk:
            p.tampilkan_info()

    def hitung_total_nilai_inventaris(self):
        total = sum(p.hitung_total() for p in self.daftar_produk)
        pajak = math.ceil(total * 0.1)  # contoh penggunaan math
        return total + pajak
