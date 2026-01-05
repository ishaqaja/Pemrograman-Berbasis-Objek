from abc import ABC, abstractmethod
from typing import List, Any


# Kontrak (Interface) untuk penyimpanan data
class BaseRepository(ABC):
    """
    Abstract Base Class untuk repository pattern.

    Class ini mendefinisikan kontrak (interface) untuk semua implementasi
    repository yang mengelola penyimpanan dan pengambilan data.
    Menerapkan prinsip Abstraction dan Dependency Inversion.
    """

    @abstractmethod
    def add(self, item: Any):
        """
        Menambahkan item baru ke dalam storage.

        Args:
            item (Any): Objek yang akan ditambahkan ke repository
        """
        pass

    @abstractmethod
    def get_all(self) -> List[Any]:
        """
        Mengambil semua item dari storage.

        Returns:
            List[Any]: List berisi semua item yang tersimpan
        """
        pass

    @abstractmethod
    def find_by_id(self, uid: str):
        """
        Mencari item berdasarkan UID.

        Args:
            uid (str): ID unik item yang dicari

        Returns:
            Any: Item yang ditemukan, atau None jika tidak ada
        """
        pass
