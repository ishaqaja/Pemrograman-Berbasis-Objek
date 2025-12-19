# class User:
#     def __init__(self, username, level):
#         self.username = username
#         self.level = level  # Level bisa diisi apa saja

#     def info(self):
#         print(f"Username: {self.username}, Level: {self.level}")


# # Membuat objek user
# user_1 = User("admin_ganteng", "Super Admin")
# user_1.info()

# # Masalah: Atribut bisa diubah seenaknya dari luar
# print("\n[Merusak data dari luar class]")
# user_1.level = 12345  # Level seharusnya string, bukan angka
# user_1.username = ""  # Username tidak boleh kosong
# user_1.info()  # Data di dalam objek menjadi tidak valid

# class User:
#     def __init__(self, username, level):
#         self.__username = username
#         self.__level = level

#     def info(self):
#         print(f"Username: {self.__username}, Level: {self.__level}")


# # --- Bagian Utama Program ---
# user_1 = User("admin_ganteng", "Super Admin")
# user_1.info()

# # Coba akses langsung atribut private dari luar
# try:
#     print(user_1.__username)
# except AttributeError as e:
#     print(f"\nError: {e}")
#     print("Atribut __username tidak bisa diakses langsung!")

# class User:
#     def __init__(self, username, level):
#         self.__username = username
#         self.__level = level

#     def info(self):
#         print(f"Username: {self.__username}, Level: {self.__level}")

#     # Getter untuk username
#     def get_username(self):
#         return self.__username

#     # Getter untuk level
#     def get_level(self):
#         return self.__level


# # --- Bagian Utama Program ---
# user_1 = User("admin_ganteng", "Super Admin")
# user_1.info()

# # Menggunakan getter untuk membaca data secara aman
# print("\n--- Mengakses data via Getter ---")
# nama_user = user_1.get_username()
# level_user = user_1.get_level()

# print(f"Username dari getter: {nama_user}")
# print(f"Level dari getter: {level_user}")

class User:
    def __init__(self, username, level):
        # Validasi awal bisa juga ditaruh di __init__ dengan memanggil setter
        self.__username = ""
        self.__level = ""
        self.set_username(username)
        self.set_level(level)

    def info(self):
        print(f"Username: {self.__username}, Level: {self.__level}")

    # --- Getter Methods ---
    def get_username(self):
        return self.__username

    def get_level(self):
        return self.__level

    # --- Setter Methods dengan Validasi ---
    def set_username(self, username_baru):
        if len(username_baru) >= 6:  # Validasi: minimal 6 karakter
            self.__username = username_baru
            print("Username berhasil diubah.")
        else:
            print("Error: Username terlalu pendek! Minimal 6 karakter.")

    def set_level(self, level_baru):
        allowed_levels = ["User", "Admin", "Super Admin"]
        if level_baru in allowed_levels:  # Validasi: level harus sesuai daftar
            self.__level = level_baru
            print("Level berhasil diubah.")
        else:
            print(f"Error: Level '{level_baru}' tidak valid!")


# --- Bagian Utama Program ---
user_1 = User("pengguna_baru", "User")
user_1.info()

print("\n--- Mencoba mengubah data via Setter ---")
user_1.set_username("adm")         # Ini akan gagal
user_1.set_level("Moderator")      # Ini akan gagal
user_1.info()                      # Data tidak berubah

print("\n--- Mencoba lagi dengan data yang valid ---")
user_1.set_username("administrator_sistem")  # Ini akan berhasil
user_1.set_level("Admin")                    # Ini akan berhasil
user_1.info()                                # Data berhasil diubah dengan aman
