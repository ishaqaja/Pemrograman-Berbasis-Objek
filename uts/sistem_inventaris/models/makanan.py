# models/makanan.py
from models.produk import Produk

class Makanan(Produk):
    def __init__(self, nama, harga, stok, kadaluarsa):
        super().__init__(nama, harga, stok)
        self.kadaluarsa = kadaluarsa

    def tampilkan_info(self):
        print(f"[Makanan] {self.nama} - Rp{self.harga} | Stok: {self.stok} | Kadaluarsa: {self.kadaluarsa}")
