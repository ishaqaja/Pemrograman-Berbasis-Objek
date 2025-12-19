from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


# ===== Model =====
@dataclass
class LeaveRequest:
    employee_name: str
    leave_days: int
    remaining_leave: int


# ===== Abstraksi (DIP) =====
class ILeaveValidationRule(ABC):
    @abstractmethod
    def validate(self, request: LeaveRequest) -> bool:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


# ===== Implementasi Aturan =====
class LeaveDaysRule(ILeaveValidationRule):
    def name(self) -> str:
        return "Validasi Jumlah Hari Cuti"

    def validate(self, request: LeaveRequest) -> bool:
        if request.leave_days <= 0:
            print("Gagal: Hari cuti tidak valid")
            return False
        if request.leave_days > request.remaining_leave:
            print("Gagal: Sisa cuti tidak cukup")
            return False
        print("Lolos: Validasi jumlah hari cuti")
        return True


class LeaveQuotaRule(ILeaveValidationRule):
    def name(self) -> str:
        return "Validasi Kuota Cuti"

    def validate(self, request: LeaveRequest) -> bool:
        if request.remaining_leave <= 0:
            print("Gagal: Tidak ada sisa cuti")
            return False
        print("Lolos: Validasi kuota cuti")
        return True


# ===== Koordinator (SRP) =====
class LeaveApprovalService:
    """
    SRP: hanya mengoordinasikan proses validasi
    DIP: bergantung pada abstraksi
    """
    def __init__(self, rules: List[ILeaveValidationRule]):
        self.rules = rules  # Dependency Injection

    def process(self, request: LeaveRequest) -> bool:
        print(f"\nProses cuti untuk {request.employee_name}")
        for rule in self.rules:
            print(f"- {rule.name()}")
            if not rule.validate(request):
                print("Hasil: CUTI DITOLAK\n")
                return False
        print("Hasil: CUTI DISETUJUI\n")
        return True


# ===== Program Utama + Challenge OCP =====
if __name__ == "__main__":
    request = LeaveRequest("Budi", 5, 10)

    service = LeaveApprovalService([
        LeaveDaysRule(),
        LeaveQuotaRule()
    ])

    print("--- Skenario 1: Validasi Dasar ---")
    service.process(request)

    # ===== Challenge: Tambah Validasi Baru (OCP) =====
    class EmployeeNameRule(ILeaveValidationRule):
        def name(self) -> str:
            return "Validasi Nama Karyawan"

        def validate(self, request: LeaveRequest) -> bool:
            if not request.employee_name.strip():
                print("Gagal: Nama kosong")
                return False
            print("Lolos: Validasi nama")
            return True

    print("--- Skenario 2: Pembuktian OCP ---")
    service_v2 = LeaveApprovalService([
        EmployeeNameRule(),
        LeaveDaysRule(),
        LeaveQuotaRule()
    ])
    service_v2.process(request)
