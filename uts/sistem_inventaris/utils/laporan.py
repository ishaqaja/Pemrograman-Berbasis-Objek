# utils/laporan.py
import os
from datetime import datetime

class Laporan:
    def __init__(self, nama_file="laporan.txt"):
        self.nama_file = nama_file

    def buat_laporan(self, inventaris):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        isi = f"LAPORAN INVENTARIS MINIMARKET\nWaktu: {waktu}\n"
        isi += "-" * 40 + "\n"

        for p in inventaris.daftar_produk:
            isi += f"{p.nama} - Stok: {p.stok} - Harga: Rp{p.harga}\n"

        total = inventaris.hitung_total_nilai_inventaris()
        isi += "-" * 40 + "\n"
        isi += f"Total Nilai Inventaris (termasuk pajak): Rp{total}\n"

        with open(self.nama_file, "w", encoding="utf-8") as file:
            file.write(isi)

        print(f"\n✅ Laporan berhasil dibuat di: {os.path.abspath(self.nama_file)}")
