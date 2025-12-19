# models/produk.py

class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"{self.nama} - Rp{self.harga} (Stok: {self.stok})")

    def hitung_total(self):
        return self.harga * self.stok
