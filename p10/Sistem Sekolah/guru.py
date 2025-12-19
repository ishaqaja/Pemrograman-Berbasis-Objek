# guru.py
from person import Person

class Guru(Person):  
    def __init__(self, nama, umur, mata_pelajaran):
        super().__init__(nama, umur)  
        self.mata_pelajaran = mata_pelajaran

    # Polymorphism: Override method perkenalan
    def perkenalan(self):
        return f"Saya Guru {self.get_nama()}, mengajar mata pelajaran {self.mata_pelajaran}."

    def nilai_siswa(self, siswa, nilai):
        siswa.set_nilai(nilai)
        print(f"Guru {self.get_nama()} memberi nilai {nilai} kepada {siswa.get_nama()}.")
