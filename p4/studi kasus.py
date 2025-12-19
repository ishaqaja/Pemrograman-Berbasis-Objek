# latihan_4.py

# Parent Class
class Kendaraan:
    def __init__(self, merk, tahun_produksi, warna):
        self.__merk = merk
        self.__tahun_produksi = tahun_produksi
        self.__warna = warna

    def tampilkan_info(self):
        print("\n--- Informasi Kendaraan ---")
        print(f"Merk           : {self.__merk}")
        print(f"Tahun Produksi : {self.__tahun_produksi}")
        print(f"Warna          : {self.__warna}")

    def nyalakan_mesin(self):
        print("Mesin kendaraan menyala.")


# Child Class - Mobil
class Mobil(Kendaraan):
    def __init__(self, merk, tahun_produksi, warna, jumlah_pintu):
        super().__init__(merk, tahun_produksi, warna)
        self.__jumlah_pintu = jumlah_pintu

    # Overriding tampilkan_info
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jumlah Pintu   : {self.__jumlah_pintu}")

    # Method spesifik mobil
    def buka_pintu_bagasi(self):
        print("Pintu bagasi terbuka!")


# Child Class - Motor
class Motor(Kendaraan):
    def __init__(self, merk, tahun_produksi, warna, kapasitas_tangki):
        super().__init__(merk, tahun_produksi, warna)
        self.__kapasitas_tangki = kapasitas_tangki

    # Overriding nyalakan_mesin
    def nyalakan_mesin(self):
        print("Brmm... Mesin motor dinyalakan dengan kick starter!")

    # Tambahan info agar motor juga punya ciri khas
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Kapasitas Tangki: {self.__kapasitas_tangki} liter")


# --- Bagian Utama Program ---
if __name__ == "__main__":
    # Membuat objek Mobil
    civic = Mobil("Honda Civic Turbo", 2021, "Hitam", 4)
    civic.tampilkan_info()
    civic.nyalakan_mesin()
    civic.buka_pintu_bagasi()

    # Membuat objek Motor
    h2 = Motor("Kawasaki H2", 2022, "Hijau", 17)
    h2.tampilkan_info()
    h2.nyalakan_mesin()
