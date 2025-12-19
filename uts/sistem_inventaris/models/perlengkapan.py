# models/perlengkapan.py
from models.produk import Produk

class Perlengkapan(Produk):
    def __init__(self, nama, harga, stok, kategori):
        super().__init__(nama, harga, stok)
        self.kategori = kategori

    def tampilkan_info(self):
        print(f"[Perlengkapan] {self.nama} - Rp{self.harga} | Stok: {self.stok} | Kategori: {self.kategori}")
