
from person import Person

class Siswa(Person): 
    def __init__(self, nama, umur, kelas):
        super().__init__(nama, umur)
        self.kelas = kelas
        self.__nilai = 0  

    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai = nilai
        else:
            print("Nilai tidak valid!")

    def get_nilai(self):
        return self.__nilai

  
    def perkenalan(self):
        return f"Saya {self.get_nama()} dari kelas {self.kelas}."

    def tampilkan_nilai(self):
        return f"{self.get_nama()} memperoleh nilai {self.__nilai}."
