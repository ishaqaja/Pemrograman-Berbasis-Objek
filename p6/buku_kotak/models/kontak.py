# models/kontak.py

class Kontak:
    def __init__(self, nama, nomor_telepon):
        self.__nama = nama
        self.__nomor_telepon = nomor_telepon

    # Method untuk menampilkan informasi kontak
    def tampilkan_info(self):
        print(f"Nama: {self.__nama}, Nomor Telepon: {self.__nomor_telepon}")

    # Getter untuk nama
    def get_nama(self):
        return self.__nama

    # Setter untuk nama
    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    # Getter untuk nomor telepon
    def get_nomor_telepon(self):
        return self.__nomor_telepon

    # Setter untuk nomor telepon
    def set_nomor_telepon(self, nomor_baru):
        self.__nomor_telepon = nomor_baru
