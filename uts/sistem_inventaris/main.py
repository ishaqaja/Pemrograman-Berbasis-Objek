# main.py
from models.makanan import Makanan
from models.minuman import Minuman
from models.perlengkapan import Perlengkapan
from models.inventaris import Inventaris
from utils.laporan import Laporan

if __name__ == "__main__":
    print("=== SISTEM INVENTARIS MINIMARKET ===")

    # Membuat objek inventaris
    inventaris = Inventaris()

    # Membuat produk (polymorphism)
    roti = Makanan("Roti Coklat", 15000, 10, "2025-12-01")
    air = Minuman("Air Mineral", 5000, 25, 600)
    sabun = Perlengkapan("Sabun Mandi", 12000, 15, "Perawatan Diri")

    # Menambahkan ke daftar inventaris
    inventaris.tambah_produk(roti)
    inventaris.tambah_produk(air)
    inventaris.tambah_produk(sabun)

    # Menampilkan semua produk
    inventaris.tampilkan_produk()

    # Menampilkan total nilai inventaris
    total = inventaris.hitung_total_nilai_inventaris()
    print(f"\nTotal Nilai Inventaris (termasuk pajak): Rp{total}")

    # Membuat laporan
    laporan = Laporan()
    laporan.buat_laporan(inventaris)
