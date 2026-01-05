from repositories.base_repository import BaseRepository
from models.entities import SumberAir
from utils.logger import logger
import datetime  # [cite: 70]


class WaterDistributionService:
    """
    Service layer untuk mengelola distribusi air.

    Class ini mengimplementasikan business logic untuk manajemen air,
    termasuk pendaftaran sumber air, pengisian, pengurangan, dan pengecekan status.
    Menerapkan prinsip Dependency Injection untuk loose coupling.

    Attributes:
        water_repo (BaseRepository): Repository untuk penyimpanan data sumber air
    """

    # Dependency Injection: Repository dimasukkan lewat constructor [cite: 68]
    def __init__(self, water_repo: BaseRepository):
        """
        Inisialisasi service dengan repository (Dependency Injection).

        Args:
            water_repo (BaseRepository): Instance repository untuk data persistence
        """
        self.water_repo = water_repo

    def daftar_sumber_air(self, sumber: SumberAir):
        """
        Mendaftarkan sumber air baru ke sistem.

        Args:
            sumber (SumberAir): Objek sumber air yang akan didaftarkan
        """
        self.water_repo.add(sumber)
        logger.info(f"Sumber air {sumber.uid} berhasil didaftarkan.")  # Logging
        print(f"✓ Truk {sumber.uid} berhasil ditambahkan dan disimpan!")

    def isi_ulang_air(self, uid_sumber: str, jumlah: float):
        """
        Mengisi ulang air ke sumber air tertentu.

        Mencari sumber air berdasarkan UID, kemudian menambah stok air
        sesuai jumlah yang diberikan. Perubahan langsung disimpan ke file.

        Args:
            uid_sumber (str): ID unik sumber air yang akan diisi
            jumlah (float): Jumlah air dalam liter yang akan ditambahkan
        """
        sumber = self.water_repo.find_by_id(uid_sumber)
        if sumber:
            try:
                # Menggunakan setter yang sudah ada validasinya
                stok_sekarang = sumber.stok_air
                sumber.stok_air = stok_sekarang + jumlah
                logger.info(
                    f"Isi ulang {jumlah}L ke {uid_sumber} berhasil. Waktu: {datetime.datetime.now()}"
                )
                # Simpan perubahan ke file
                (
                    self.water_repo.save_to_file()
                    if hasattr(self.water_repo, "save_to_file")
                    else None
                )
                print(
                    f"✓ Berhasil mengisi {jumlah}L air. Stok sekarang: {sumber.stok_air}L"
                )
            except ValueError as e:
                logger.error(f"Gagal isi ulang: {e}")
        else:
            logger.warning(f"Sumber air {uid_sumber} tidak ditemukan.")

    def kurangi_air(self, uid_sumber: str, jumlah: float):
        """
        Mengurangi isi air dari sumber air (misalnya untuk distribusi ke warga).

        Mencari sumber air berdasarkan UID, memvalidasi ketersediaan stok,
        kemudian mengurangi stok air. Perubahan langsung disimpan ke file.
        Akan menampilkan error jika stok tidak mencukupi.

        Args:
            uid_sumber (str): ID unik sumber air yang akan dikurangi
            jumlah (float): Jumlah air dalam liter yang akan dikurangi
        """
        sumber = self.water_repo.find_by_id(uid_sumber)
        if sumber:
            try:
                stok_sekarang = sumber.stok_air
                if jumlah > stok_sekarang:
                    logger.error(
                        f"Gagal kurangi air: Jumlah {jumlah}L melebihi stok ({stok_sekarang}L)"
                    )
                    print(
                        f"❌ Stok air tidak mencukupi! Stok saat ini: {stok_sekarang}L"
                    )
                else:
                    sumber.stok_air = stok_sekarang - jumlah
                    # Simpan perubahan ke file
                    (
                        self.water_repo.save_to_file()
                        if hasattr(self.water_repo, "save_to_file")
                        else None
                    )
                    logger.info(
                        f"Kurangi {jumlah}L dari {uid_sumber} berhasil. Sisa: {sumber.stok_air}L. Waktu: {datetime.datetime.now()}"
                    )
                    print(
                        f"✓ Berhasil mengurangi {jumlah}L air. Sisa stok: {sumber.stok_air}L"
                    )
            except ValueError as e:
                logger.error(f"Gagal kurangi air: {e}")
        else:
            logger.warning(f"Sumber air {uid_sumber} tidak ditemukan.")
            print(f"❌ Truk dengan ID {uid_sumber} tidak ditemukan.")

    def cek_status_semua(self):
        """
        Menampilkan status semua sumber air yang terdaftar.

        Mengambil semua sumber air dari repository dan menampilkan
        informasi detail masing-masing sumber air ke console.
        """
        semua_sumber = self.water_repo.get_all()
        print("\n--- STATUS KETERSEDIAAN AIR ---")
        for s in semua_sumber:
            print(s.info())
