# latihan_3.py

class Karyawan:
    def __init__(self, nama, id_karyawan, gaji):
        # atribut privat
        self.__nama = nama
        self.__id_karyawan = id_karyawan
        self.__gaji = gaji

    # Getter
    def get_nama(self):
        return self.__nama

    def get_id(self):
        return self.__id_karyawan

    def get_gaji(self):
        return self.__gaji

    # Setter
    def set_nama(self, nama_baru):
        if nama_baru.strip() != "":
            self.__nama = nama_baru
        else:
            print("Error: Nama tidak boleh kosong!")

    def set_gaji(self, gaji_baru):
        if isinstance(gaji_baru, (int, float)) and gaji_baru > 0:
            self.__gaji = gaji_baru
        else:
            print("Error: Gaji harus berupa angka positif!")

# Bagian utama program
if __name__ == "__main__":
    # a. Membuat objek Karyawan dengan data awal yang valid
    karyawan1 = Karyawan("Muhammad Ishaq", "EMP01", 6000000)

    # b. Menampilkan informasi lengkap karyawan dengan getter
    print("=== Informasi Karyawan ===")
    print("Nama       :", karyawan1.get_nama())
    print("ID         :", karyawan1.get_id())
    print("Gaji       :", karyawan1.get_gaji())

    # c. Coba ubah gaji menjadi nilai negatif
    print("\nCoba set gaji ke -7000000:")
    karyawan1.set_gaji(-7000000)

    # d. Coba ubah nama menjadi string kosong
    print("\nCoba set nama ke string kosong:")
    karyawan1.set_nama("")

    # e. Ubah gaji menjadi nilai positif valid
    print("\nCoba set gaji ke 8000000:")
    karyawan1.set_gaji(8000000)

    # f. Tampilkan informasi terbaru
    print("\n=== Informasi Karyawan Setelah Update ===")
    print("Nama       :", karyawan1.get_nama())
    print("ID         :", karyawan1.get_id())
    print("Gaji       :", karyawan1.get_gaji())
