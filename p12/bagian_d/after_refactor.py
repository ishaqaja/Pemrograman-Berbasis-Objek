import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


# ===== KONFIGURASI LOGGING =====
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

LOGGER = logging.getLogger("LeaveApproval")


# ===== Model =====
@dataclass
class LeaveRequest:
    """
    Merepresentasikan permintaan cuti karyawan.

    Args:
        employee_name (str): Nama karyawan.
        leave_days (int): Jumlah hari cuti yang diajukan.
        remaining_leave (int): Sisa kuota cuti karyawan.
    """
    employee_name: str
    leave_days: int
    remaining_leave: int


# ===== Abstraksi (DIP) =====
class ILeaveValidationRule(ABC):
    """
    Kontrak untuk semua aturan validasi cuti.
    """

    @abstractmethod
    def validate(self, request: LeaveRequest) -> bool:
        """
        Memvalidasi permintaan cuti.

        Args:
            request (LeaveRequest): Permintaan cuti.

        Returns:
            bool: True jika valid, False jika tidak.
        """
        pass

    @abstractmethod
    def name(self) -> str:
        """Mengembalikan nama aturan validasi."""
        pass


# ===== Implementasi Aturan =====
class LeaveDaysRule(ILeaveValidationRule):
    """Validasi jumlah hari cuti yang diajukan."""

    def name(self) -> str:
        return "Validasi Jumlah Hari Cuti"

    def validate(self, request: LeaveRequest) -> bool:
        if request.leave_days <= 0:
            LOGGER.warning("Gagal: Hari cuti tidak valid")
            return False
        if request.leave_days > request.remaining_leave:
            LOGGER.warning("Gagal: Sisa cuti tidak cukup")
            return False
        LOGGER.info("Lolos: Validasi jumlah hari cuti")
        return True


class LeaveQuotaRule(ILeaveValidationRule):
    """Validasi kuota cuti karyawan."""

    def name(self) -> str:
        return "Validasi Kuota Cuti"

    def validate(self, request: LeaveRequest) -> bool:
        if request.remaining_leave <= 0:
            LOGGER.warning("Gagal: Tidak ada sisa cuti")
            return False
        LOGGER.info("Lolos: Validasi kuota cuti")
        return True


# ===== Koordinator (SRP) =====
class LeaveApprovalService:
    """
    Mengoordinasikan proses validasi cuti karyawan.

    Class ini hanya bertanggung jawab mengatur alur validasi
    dan bergantung pada abstraksi aturan validasi (SRP & DIP).
    """

    def __init__(self, rules: List[ILeaveValidationRule]):
        """
        Menginisialisasi layanan persetujuan cuti.

        Args:
            rules (List[ILeaveValidationRule]): Daftar aturan validasi.
        """
        self.rules = rules

    def process(self, request: LeaveRequest) -> bool:
        """
        Memproses permintaan cuti berdasarkan aturan validasi.

        Args:
            request (LeaveRequest): Permintaan cuti.

        Returns:
            bool: True jika disetujui, False jika ditolak.
        """
        LOGGER.info(f"Proses cuti untuk {request.employee_name}")

        for rule in self.rules:
            LOGGER.info(f"Menjalankan: {rule.name()}")
            if not rule.validate(request):
                LOGGER.warning("Hasil: CUTI DITOLAK")
                return False

        LOGGER.info("Hasil: CUTI DISETUJUI")
        return True


# ===== Program Utama + Pembuktian OCP =====
if __name__ == "__main__":
    request = LeaveRequest("Budi", 5, 10)

    service = LeaveApprovalService([
        LeaveDaysRule(),
        LeaveQuotaRule()
    ])

    LOGGER.info("--- Skenario 1: Validasi Dasar ---")
    service.process(request)

    # ===== Challenge OCP =====
    class EmployeeNameRule(ILeaveValidationRule):
        """Validasi nama karyawan."""

        def name(self) -> str:
            return "Validasi Nama Karyawan"

        def validate(self, request: LeaveRequest) -> bool:
            if not request.employee_name.strip():
                LOGGER.warning("Gagal: Nama karyawan kosong")
                return False
            LOGGER.info("Lolos: Validasi nama karyawan")
            return True

    LOGGER.info("--- Skenario 2: Pembuktian OCP ---")
    service_v2 = LeaveApprovalService([
        EmployeeNameRule(),
        LeaveDaysRule(),
        LeaveQuotaRule()
    ])

    service_v2.process(request)
