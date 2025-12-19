import os
from datetime import datetime


current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)  # Ubah working directory ke folder file ini


class FileAnalyzer:
    def __init__(self, file_path):
        self.__file_path = file_path
        if os.path.exists(file_path):
            self.__file_ada = True
            self.__ukuran_file = os.path.getsize(file_path)
        else:
            self.__file_ada = False
            print(f"File '{file_path}' tidak ditemukan.")
    
    def get_file_size(self, unit="bytes"):
        """Mengembalikan ukuran file dalam bytes atau KB."""
        if not self.__file_ada:
            return None
        
        if unit.lower() == "kb":
            return self.__ukuran_file / 1024
        return self.__ukuran_file
    
    def get_modification_time(self):
        """Mengembalikan waktu modifikasi terakhir dalam format terbaca manusia."""
        if not self.__file_ada:
            return None
        
        waktu_modifikasi = os.path.getmtime(self.__file_path)
        return datetime.fromtimestamp(waktu_modifikasi).strftime("%d %B %Y, %H:%M:%S")
    
    def analyze(self):
        """Menganalisis file dan mencetak informasi lengkap."""
        print("\n=== HASIL ANALISIS FILE ===")
        print(f"Nama File   : {self.__file_path}")
        
        if not self.__file_ada:
            print("Status      : File tidak ditemukan. Tidak dapat dianalisis.")
            print("==============================\n")
            return
        
        print("Status      : File ditemukan")
        print(f"Ukuran File : {self.get_file_size('KB'):.2f} KB")
        print(f"Diperbarui  : {self.get_modification_time()}")
        print("==============================\n")


# --- Bagian utama program ---
if __name__ == "__main__":
    # File yang ada
    analyzer1 = FileAnalyzer("dokumen.txt")
    analyzer1.analyze()

    # (Opsional) File yang tidak ada
    analyzer2 = FileAnalyzer("file_khayalan.txt")
    analyzer2.analyze()

# import math # Impor pustaka math

# class KalkulatorLingkaran:
#     def __init__(self, radius):
#         self._radius = 0
#         self.set_radius(radius)
#         print(f"Objek lingkaran dengan radius {self._radius} dibuat.")

#     def set_radius(self, radius):
#         if radius > 0:
#             self._radius = radius
#         else:
#             print("Error: Radius harus lebih besar dari 0.")
#             self._radius = 1 # Nilai default jika input salah

#     def hitung_luas(self):
#         # Menggunakan konstanta pi dari pustaka math
#         luas = math.pi * (self._radius ** 2)
#         return luas

#     def hitung_keliling(self):
#         # Menggunakan konstanta pi lagi
#         keliling = 2 * math.pi * self._radius
#         return keliling

# # --- Bagian Utama Program ---
# lingkaran_1 = KalkulatorLingkaran(7)
# luas_lingkaran = lingkaran_1.hitung_luas()
# keliling_lingkaran = lingkaran_1.hitung_keliling()

# print(f"\nRadius: 7")
# print(f"Luas Lingkaran: {luas_lingkaran:.2f}") # Format 2 angka di belakang koma
# print(f"Keliling Lingkaran: {keliling_lingkaran:.2f}")

# import datetime
# class LogPesan:
#     def __init__(self, pengirim, isi_pesan):
#         self._pengirim = pengirim
#         self._isi_pesan = isi_pesan
#         # Secara otomatis mendapatkan waktu saat ini ketika objek dibuat
#         self._timestamp = datetime.datetime.now()


#     def tampilkan_log(self):
#         # Memformat timestamp menjadi string yang mudah dibaca
#         waktu_terformat = self._timestamp.strftime("%d %B %Y, Pukul %H:%M:%S")
#         print("--- Log Pesan Masuk ---")
#         print(f"Pengirim  : {self._pengirim}")
#         print(f"Waktu     : {waktu_terformat}")
#         print(f"Pesan     : {self._isi_pesan}")


# # --- Bagian Utama Program ---
# pesan_1 = LogPesan("Admin", "Server akan segera di-restart untuk maintenance.")
# pesan_1.tampilkan_log()

# # Tunggu beberapa detik dan buat pesan lain
# # (Untuk simulasi, kita bisa tambahkan time.sleep jika diinginkan)
# pesan_2 = LogPesan("User01", "Pekerjaan saya sudah disimpan, silakan restart.")
# pesan_2.tampilkan_log()