import math

# Menghitung akar kuadrat
angka = 16
akar = math.sqrt(angka)
print(f"Akar kuadrat dari {angka} adalah {akar}")

# Menghitung pangkat
hasil = math.pow(2, 3)
print(f"2 pangkat 3 adalah {hasil}")


import datetime

# Mendapatkan waktu sekarang
waktu_sekarang = datetime.datetime.now()
print(f"Waktu sekarang: {waktu_sekarang}")

# Menggunakan timedelta untuk menghitung selisih waktu
hari_ini = datetime.datetime.now()
satu_hari = datetime.timedelta(days=1)
besok = hari_ini + satu_hari
print(f"besok adalah: {besok}")


import os

# Cek apakah file atau direktori ada
file_path = "data.txt"
if os.path.exists(file_path):
    print(f"File {file_path} ditemukan.")
else:
    print(f"File {file_path} tidak ditemukan.")


    # Menulis ke dalam file
with open("data.txt", "w") as file:
    file.write("Halo, ini adalah file teks!")

# Membaca file yang telah ditulis
with open("data.txt", "r") as file:
    konten = file.read()
    print(konten)


 import requests

# Mengirim permintaan GET ke API
response = requests.get("https://api.github.com")
print(response.json()) # Menampilkan respons dalam format JSON