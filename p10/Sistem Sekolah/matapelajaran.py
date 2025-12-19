# matapelajaran.py

class MataPelajaran:
    def __init__(self, nama, kode):
        self.nama = nama
        self.kode = kode
        self.guru_pengampu = None

    def set_guru_pengampu(self, guru):
        self.guru_pengampu = guru
        print(f"Guru {guru.get_nama()} ditetapkan sebagai pengampu {self.nama}.")

    def tampilkan_info(self):
        pengampu = self.guru_pengampu.get_nama() if self.guru_pengampu else "Belum ditentukan"
        return f"{self.nama} ({self.kode}), Pengampu: {pengampu}"
