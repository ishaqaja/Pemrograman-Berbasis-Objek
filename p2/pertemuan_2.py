
class Buku:
    # Constructor
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.status_pinjam = False  

    # Method menampilkan informasi buku
    def tampilkan_info(self):
        status = "Dipinjam" if self.status_pinjam else "Tersedia"
        print("\n--- Informasi Buku ---")
        print(f"Judul        : {self.judul}")
        print(f"Penulis      : {self.penulis}")
        print(f"Tahun Terbit : {self.tahun_terbit}")
        print(f"Status       : {status}")
        print("-----------------------")

    # Method meminjam buku
    def pinjam_buku(self):
        if not self.status_pinjam:
            self.status_pinjam = True
            print(f"Buku '{self.judul}' telah dipinjam.")
        else:
            print(f"Maaf, buku '{self.judul}' sedang dipinjam.")

    # Method mengembalikan buku
    def kembalikan_buku(self):
        if self.status_pinjam:
            self.status_pinjam = False
            print(f"Buku '{self.judul}' telah dikembalikan.")
        else:
            print(f"Buku '{self.judul}' buku sudah tersedia.")


# Membuat objek buku
buku1 = Buku("Psychology Of Money", "Morgan Housel", 2020)
buku2 = Buku("Atomic Habbit", "James Clear", 2018)


# Menampilkan status awal buku
buku1.tampilkan_info()
buku2.tampilkan_info()

# Simulasi peminjaman buku
print("\n--- Proses Peminjaman ---")
buku1.pinjam_buku()
buku1.tampilkan_info()

# Simulasi pengembalian buku
print("\n--- Proses Pengembalian ---")
buku1.kembalikan_buku()
buku1.tampilkan_info()
