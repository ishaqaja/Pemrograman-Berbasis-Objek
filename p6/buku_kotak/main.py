# main.py

from models.kontak import Kontak

if __name__ == "__main__":
    # Membuat list kosong untuk menyimpan daftar kontak
    daftar_kontak = []

    # Membuat tiga objek Kontak
    kontak1 = Kontak("Ishaq", "081234567890")
    kontak2 = Kontak("yusuf", "082233445566")
    kontak3 = Kontak("Husain", "083322110099")

    # Menambahkan kontak ke dalam daftar
    daftar_kontak.extend([kontak1, kontak2, kontak3])

    # Menampilkan semua kontak
    print("=== Daftar Kontak ===")
    for kontak in daftar_kontak:
        kontak.tampilkan_info()
