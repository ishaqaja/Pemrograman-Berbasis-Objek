
from guru import Guru
from siswa import Siswa
from matapelajaran import MataPelajaran


guru1 = Guru("Pak Budi", 35, "Matematika")
siswa1 = Siswa("ishaq", 20, "XII IPA 1")


mapel1 = MataPelajaran("Matematika", "MTK101")
mapel1.set_guru_pengampu(guru1)


print(guru1.perkenalan())   
print(siswa1.perkenalan()) 
guru1.nilai_siswa(siswa1, 95) 


print(siswa1.tampilkan_nilai())
print(mapel1.tampilkan_info())
