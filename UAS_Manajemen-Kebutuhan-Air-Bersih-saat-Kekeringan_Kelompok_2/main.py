"""Application entry point untuk sistem manajemen air bersih.

Script ini menyediakan interface CLI untuk mengelola distribusi air
melalui armada truk tangki, termasuk fitur:
- Pendaftaran truk baru
- Pengisian ulang air
- Penggunaan/distribusi air
- Monitoring status air

Data disimpan secara persisten ke file JSON.
"""

from models.entities import TrukTangki
from repositories.file_repository import FileRepository
from services.water_service import WaterDistributionService
from utils.logger import logger


def main():
    """
    Fungsi utama aplikasi manajemen air bersih.

    Menginisialisasi komponen sistem (repository dan service),
    kemudian menjalankan loop interaktif untuk menerima input
    pengguna dan menjalankan operasi yang sesuai.
    """
    logger.info("Aplikasi Manajemen Air Bersih Dimulai...")

    # 1. Setup Dependency Injection
    # Kita buat repository dengan file persistence
    repo_air = FileRepository("data_truk.json")

    # Kita masukkan wadah data ke service (logika)
    service = WaterDistributionService(repo_air)

    print(
        f"\n📂 Data dimuat dari file. Total truk terdaftar: {len(repo_air.get_all())}"
    )

    # 2. Simulasi Interaksi User (CLI Loop bisa ditambahkan di sini)
    while True:
        print("\n=== MENU POSKO KEKERINGAN ===")
        print("1. Tambah Armada Truk Air")
        print("2. Isi Ulang Air")
        print("3. Gunakan Air dari Truk")
        print("4. Cek Status Air")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            uid = input("ID Truk: ")
            plat = input("Plat Nomor: ")
            kap = float(input("Kapasitas (Liter): "))
            truk_baru = TrukTangki(uid, plat, kap)
            service.daftar_sumber_air(truk_baru)

        elif pilihan == "2":
            uid = input("ID Truk yang diisi: ")
            jml = float(input("Jumlah Air (Liter): "))
            service.isi_ulang_air(uid, jml)

        elif pilihan == "3":
            uid = input("ID Truk yang akan digunakan: ")
            jml = float(input("Jumlah Air yang akan digunakan (Liter): "))
            service.kurangi_air(uid, jml)

        elif pilihan == "4":
            service.cek_status_semua()

        elif pilihan == "5":
            logger.info("Aplikasi ditutup.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
