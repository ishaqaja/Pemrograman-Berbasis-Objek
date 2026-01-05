from .base_model import Identifiable


# Penerapan Inheritance (Identifiable -> SumberAir)
class SumberAir(Identifiable):
    """
    Class untuk merepresentasikan sumber air yang dapat menyimpan air.

    Class ini menerapkan prinsip Inheritance dari Identifiable dan Enkapsulasi
    dengan menggunakan private attribute untuk stok air.

    Attributes:
        uid (str): ID unik sumber air (dari parent class)
        lokasi (str): Lokasi sumber air
        _kapasitas_max (float): Kapasitas maksimum air dalam liter (protected)
        __stok_air (float): Stok air saat ini dalam liter (private, enkapsulasi)
    """

    def __init__(self, uid: str, lokasi: str, kapasitas_max: float):
        """
        Inisialisasi sumber air dengan parameter yang diberikan.

        Args:
            uid (str): ID unik untuk sumber air
            lokasi (str): Lokasi sumber air
            kapasitas_max (float): Kapasitas maksimum air dalam liter
        """
        super().__init__(uid)
        self.lokasi = lokasi
        self._kapasitas_max = kapasitas_max
        self.__stok_air = 0.0  # Private attribute (Enkapsulasi) [cite: 57]

    # Getter (Akses data private) [cite: 58]
    @property
    def stok_air(self):
        """
        Getter untuk mengakses stok air (enkapsulasi).

        Returns:
            float: Jumlah stok air saat ini dalam liter
        """
        return self.__stok_air

    # Setter dengan Validasi [cite: 58]
    @stok_air.setter
    def stok_air(self, jumlah: float):
        """
        Setter untuk mengatur stok air dengan validasi.

        Validasi memastikan stok tidak negatif dan tidak melebihi kapasitas.
        Jika melebihi kapasitas, stok akan diset ke kapasitas maksimum.

        Args:
            jumlah (float): Jumlah air yang akan diset dalam liter

        Raises:
            ValueError: Jika jumlah bernilai negatif
        """
        if jumlah < 0:
            raise ValueError("Stok air tidak boleh negatif.")
        if jumlah > self._kapasitas_max:
            self.__stok_air = self._kapasitas_max
        else:
            self.__stok_air = jumlah

    # Polymorphism (Override method info) [cite: 62]
    def info(self):
        """
        Menampilkan informasi sumber air (implementasi dari abstract method).

        Menerapkan prinsip Polymorphism dengan meng-override method dari parent class.

        Returns:
            str: String berisi informasi lokasi dan stok air
        """
        return f"Sumber Air di {self.lokasi} | Stok: {self.__stok_air}/{self._kapasitas_max} L"


class TrukTangki(SumberAir):
    """
    Class untuk merepresentasikan truk tangki air.

    Class ini merupakan turunan dari SumberAir yang menerapkan prinsip
    Inheritance dan Polymorphism dengan spesialisasi untuk truk tangki.

    Attributes:
        uid (str): ID unik truk (dari grandparent class)
        lokasi (str): Selalu "Mobil" untuk truk (dari parent class)
        _kapasitas_max (float): Kapasitas tangki dalam liter (dari parent class)
        plat_nomor (str): Nomor plat kendaraan truk
    """

    def __init__(self, uid: str, plat_nomor: str, kapasitas: float):
        """
        Inisialisasi truk tangki dengan parameter yang diberikan.

        Args:
            uid (str): ID unik untuk truk
            plat_nomor (str): Nomor plat kendaraan
            kapasitas (float): Kapasitas tangki dalam liter
        """
        super().__init__(uid, "Mobil", kapasitas)
        self.plat_nomor = plat_nomor

    # Polymorphism: Truk punya info spesifik
    def info(self):
        """
        Menampilkan informasi truk tangki (polymorphism).

        Meng-override method info() dari parent class untuk menambahkan
        informasi spesifik truk yaitu nomor plat.

        Returns:
            str: String berisi nomor plat dan informasi detail truk
        """
        base_info = super().info()
        return f"[TRUK {self.plat_nomor}] {base_info}"
