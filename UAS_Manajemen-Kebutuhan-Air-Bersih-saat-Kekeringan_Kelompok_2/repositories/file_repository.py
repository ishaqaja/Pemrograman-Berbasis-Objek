from .base_repository import BaseRepository
from models.entities import TrukTangki, SumberAir
from utils.logger import logger
from typing import List, Any
import json
import os


class FileRepository(BaseRepository):
    """
    Repository dengan penyimpanan persisten ke file JSON.

    Implementasi dari BaseRepository yang menyimpan data ke file JSON
    untuk persistensi data. Mendukung auto-save setiap ada perubahan data.

    Attributes:
        _storage (List): List internal untuk menyimpan objek di memory
        file_path (str): Path ke file JSON untuk penyimpanan
    """

    def __init__(self, file_path: str = "data_truk.json"):
        """
        Inisialisasi repository dan memuat data dari file.

        Args:
            file_path (str): Path ke file JSON. Default: "data_truk.json"
        """
        self._storage = []
        self.file_path = file_path
        self.load_from_file()

    def add(self, item: Any):
        """
        Menambah item baru dan langsung menyimpan ke file.

        Args:
            item (Any): Objek yang akan ditambahkan (harus punya atribut uid)
        """
        self._storage.append(item)
        self.save_to_file()
        logger.info(f"Data {item.uid} ditambahkan dan disimpan ke file.")

    def get_all(self) -> List[Any]:
        """
        Mengambil semua item dari storage.

        Returns:
            List[Any]: List berisi semua item yang tersimpan
        """
        return self._storage

    def find_by_id(self, uid: str):
        """
        Mencari item berdasarkan UID.

        Args:
            uid (str): ID unik item yang dicari

        Returns:
            Any: Item yang ditemukan, atau None jika tidak ditemukan
        """
        for item in self._storage:
            if item.uid == uid:
                return item
        return None

    def update(self, item: Any):
        """
        Update item yang sudah ada dan simpan ke file.

        Args:
            item (Any): Objek baru yang akan menggantikan objek lama dengan UID sama

        Returns:
            bool: True jika berhasil update, False jika item tidak ditemukan
        """
        for i, stored_item in enumerate(self._storage):
            if stored_item.uid == item.uid:
                self._storage[i] = item
                self.save_to_file()
                logger.info(f"Data {item.uid} diupdate dan disimpan ke file.")
                return True
        return False

    def save_to_file(self):
        """
        Menyimpan semua data ke file JSON.

        Melakukan serialisasi objek menjadi dictionary dan menyimpannya
        ke file JSON dengan format yang mudah dibaca (indented).
        Mendukung objek TrukTangki dan SumberAir.

        Raises:
            Exception: Jika terjadi error saat menulis ke file
        """
        try:
            data_to_save = []
            for item in self._storage:
                if isinstance(item, TrukTangki):
                    data_to_save.append(
                        {
                            "type": "TrukTangki",
                            "uid": item.uid,
                            "plat_nomor": item.plat_nomor,
                            "kapasitas_max": item._kapasitas_max,
                            "stok_air": item.stok_air,
                        }
                    )
                elif isinstance(item, SumberAir):
                    data_to_save.append(
                        {
                            "type": "SumberAir",
                            "uid": item.uid,
                            "lokasi": item.lokasi,
                            "kapasitas_max": item._kapasitas_max,
                            "stok_air": item.stok_air,
                        }
                    )

            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data_to_save, f, indent=4, ensure_ascii=False)

            logger.info(f"Data berhasil disimpan ke {self.file_path}")
        except Exception as e:
            logger.error(f"Gagal menyimpan data ke file: {e}")

    def load_from_file(self):
        """
        Memuat data dari file JSON ke memory.

        Melakukan deserialisasi data dari file JSON menjadi objek
        TrukTangki atau SumberAir. Jika file tidak ada atau corrupt,
        akan memulai dengan storage kosong.

        Raises:
            json.JSONDecodeError: Jika format JSON tidak valid
            Exception: Jika terjadi error lain saat membaca file
        """
        if not os.path.exists(self.file_path):
            logger.info(f"File {self.file_path} tidak ditemukan. Membuat file baru.")
            self._storage = []
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self._storage = []
            for item_data in data:
                if item_data["type"] == "TrukTangki":
                    truk = TrukTangki(
                        uid=item_data["uid"],
                        plat_nomor=item_data["plat_nomor"],
                        kapasitas=item_data["kapasitas_max"],
                    )
                    truk.stok_air = item_data["stok_air"]
                    self._storage.append(truk)
                elif item_data["type"] == "SumberAir":
                    sumber = SumberAir(
                        uid=item_data["uid"],
                        lokasi=item_data["lokasi"],
                        kapasitas_max=item_data["kapasitas_max"],
                    )
                    sumber.stok_air = item_data["stok_air"]
                    self._storage.append(sumber)

            logger.info(
                f"Berhasil memuat {len(self._storage)} data dari {self.file_path}"
            )
        except json.JSONDecodeError:
            logger.warning(
                f"File {self.file_path} kosong atau format tidak valid. Memulai dengan data kosong."
            )
            self._storage = []
        except Exception as e:
            logger.error(f"Gagal memuat data dari file: {e}")
            self._storage = []
