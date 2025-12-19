# PARENT CLASS
class Bentuk:
    def gambar(self):
        # Method ini sengaja dibuat umum dan akan di-override
        raise NotImplementedError("Subclass harus mengimplementasikan method ini!")

# CHILD CLASS 1
class Persegi(Bentuk):
    def gambar(self):
        print("Menggambar Persegi: [][][]")

# CHILD CLASS 2
class Lingkaran(Bentuk):
    def gambar(self):
        print("Menggambar Lingkaran: OOOOOO")

# ... (setelah definisi class-class sebelumnya)

# CHILD CLASS 3
class Segitiga(Bentuk):
    def gambar(self):
        print("Menggambar Segitiga: /\\")

# CLASS YANG TIDAK BERHUBUNGAN (untuk Duck Typing)
class Teks:
    def gambar(self):
        print("Menulis Teks: 'Hello, Polymorphism!'")

# Sebuah fungsi yang menunjukkan perilaku polimorfik
def render_objek(objek_untuk_digambar):
    print("Mencoba me-render objek...")
    objek_untuk_digambar.gambar()


# --- Bagian Utama Program ---
# --- Bagian Utama Program ---
# Membuat list yang berisi objek-objek dari class yang berbeda
daftar_bentuk = [Persegi(), Lingkaran(), Persegi(), Lingkaran()]

print("--- Memanggil method yang sama pada objek yang berbeda ---")
# Iterasi melalui list dan panggil method .gambar() pada setiap objek
for bentuk in daftar_bentuk:
    bentuk.gambar() # Satu pemanggilan, banyak bentuk/perilaku!
    
persegi = Persegi()
lingkaran = Lingkaran()
segitiga = Segitiga()
teks_biasa = Teks() # Objek ini BUKAN turunan dari Bentuk

print("\n--- Menggunakan fungsi polimorfik ---")
render_objek(persegi)
render_objek(lingkaran)
render_objek(segitiga)

print("\n--- Demonstrasi Duck Typing ---")
render_objek(teks_biasa) # Fungsi tetap bekerja!

