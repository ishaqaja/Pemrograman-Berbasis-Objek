from dataclasses import dataclass

@dataclass
class LeaveRequest:
    employee_name: str
    leave_days: int
    remaining_leave: int


class LeaveValidationManager:
    # God Class: semua validasi digabung & pakai if/else
    def validate(self, request: LeaveRequest, validation_type: str) -> bool:
        print(f"Validasi cuti untuk {request.employee_name}")

        if validation_type == "leave_days":
            if request.leave_days <= 0:
                print("Gagal: Jumlah hari cuti tidak valid")
                return False
            if request.leave_days > request.remaining_leave:
                print("Gagal: Sisa cuti tidak mencukupi")
                return False
            print("Lolos: Validasi jumlah cuti")
            return True

        elif validation_type == "quota":
            if request.remaining_leave <= 0:
                print("Gagal: Tidak ada sisa cuti")
                return False
            print("Lolos: Validasi kuota cuti")
            return True

        else:
            print("Tipe validasi tidak dikenal")
            return False


if __name__ == "__main__":
    req = LeaveRequest("Budi", 5, 10)
    manager = LeaveValidationManager()

    manager.validate(req, "leave_days")
    manager.validate(req, "quota")
