# models/minuman.py
from models.produk import Produk

class Minuman(Produk):
    def __init__(self, nama, harga, stok, volume):
        super().__init__(nama, harga, stok)
        self.volume = volume

    def tampilkan_info(self):
        print(f"[Minuman] {self.nama} - Rp{self.harga} | Stok: {self.stok} | Volume: {self.volume}ml")
