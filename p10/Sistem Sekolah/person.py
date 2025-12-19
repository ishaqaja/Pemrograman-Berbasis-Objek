

class Person:
    def __init__(self, nama, umur):
        self.__nama = nama     
        self.__umur = umur

  
    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        if len(nama) > 2:
            self.__nama = nama
        else:
            print("Nama terlalu pendek!")

    def get_umur(self):
        return self.__umur

    def set_umur(self, umur):
        if umur > 5:
            self.__umur = umur
        else:
            print("Umur tidak valid!")


    def perkenalan(self):
        return f"Halo, nama saya {self.__nama}, saya berumur {self.__umur} tahun."
