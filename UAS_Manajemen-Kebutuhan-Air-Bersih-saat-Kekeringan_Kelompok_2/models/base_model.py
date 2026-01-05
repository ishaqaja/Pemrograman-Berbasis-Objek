from abc import ABC, abstractmethod


# Penerapan Abstraction
class Identifiable(ABC):
    """
    Class abstrak untuk objek yang dapat diidentifikasi dengan UID unik.

    Class ini menerapkan prinsip Abstraction dalam OOP, menyediakan
    kontrak dasar untuk semua objek yang memerlukan identifikasi unik.

    Attributes:
        _uid (str): ID unik yang bersifat protected untuk identifikasi objek
    """

    def __init__(self, uid: str):
        """
        Inisialisasi objek dengan UID unik.

        Args:
            uid (str): ID unik untuk mengidentifikasi objek
        """
        self._uid = uid  # Protected attribute

    @property
    def uid(self):
        """
        Getter untuk mengakses UID objek.

        Returns:
            str: ID unik objek
        """
        return self._uid

    @abstractmethod
    def info(self):
        """
        Method abstrak untuk menampilkan informasi objek.

        Method ini harus diimplementasikan oleh class turunan untuk
        menampilkan informasi spesifik sesuai dengan jenis objek.

        Returns:
            str: Informasi detail tentang objek
        """
        pass
