# latihan_5.py

# Parent Class Abstrak
class Notifikasi:
    def kirim(self, pesan):
        raise NotImplementedError("Subclass harus mengimplementasikan method ini!")


# Child Class Email
class Email(Notifikasi):
    def kirim(self, pesan):
        print(f"[EMAIL] Mengirim: '{pesan}'")


# Child Class SMS
class SMS(Notifikasi):
    def kirim(self, pesan):
        print(f"[SMS] Mengirim: '{pesan}'")


# Child Class Push Notification
class PushNotif(Notifikasi):
    def kirim(self, pesan):
        print(f"[PUSH] Mengirim: '{pesan}'")


# Bagian utama program
if __name__ == "__main__":
    # Membuat list notifikasi
    daftar_notifikasi = [
        Email(),
        SMS(),
        PushNotif()
    ]

    # Pesan yang ingin dikirim
    pesan = "Diskon Spesial! Hanya untuk kamu!"

    # Loop polymorphism
    for notif in daftar_notifikasi:
        notif.kirim(pesan)
