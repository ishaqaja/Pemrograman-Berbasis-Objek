# Refactoring SOLID – Sistem Validasi Pengajuan Cuti Karyawan

## Deskripsi
Project ini merupakan latihan refactoring kode berorientasi objek (OOP) dengan menerapkan prinsip desain **SOLID**, khususnya **Single Responsibility Principle (SRP)**, **Open/Closed Principle (OCP)**, dan **Dependency Inversion Principle (DIP)**. Studi kasus yang digunakan adalah **Sistem Validasi Pengajuan Cuti Karyawan** yang pada awalnya memiliki struktur kode kaku (rigid) dan mengandung code smell berupa God Class dan penggunaan method if/else yang berlebihan.

---

## Studi Kasus
Sistem melakukan validasi pengajuan cuti karyawan berdasarkan beberapa aturan, seperti:
- Validasi jumlah hari cuti
- Validasi kuota cuti
- (Challenge) Validasi tambahan tanpa mengubah kode lama

---

## Analisis Kode Sebelum Refactoring

### 1. Pelanggaran Single Responsibility Principle (SRP)
Kelas `LeaveValidationManager` memiliki lebih dari satu tanggung jawab, yaitu:
- Melakukan validasi jumlah hari cuti
- Melakukan validasi kuota cuti
- Menentukan jenis validasi menggunakan parameter dan struktur if/else  

Hal ini menyebabkan satu kelas memiliki banyak alasan untuk berubah.

---

### 2. Pelanggaran Open/Closed Principle (OCP)
Untuk menambahkan jenis validasi baru, pengembang harus memodifikasi method `validate()` dengan menambahkan kondisi `elif` baru. Artinya, kelas tidak tertutup terhadap perubahan dan setiap penambahan fitur berisiko merusak kode yang sudah ada.

---

### 3. Pelanggaran Dependency Inversion Principle (DIP)
Logika utama validasi bergantung langsung pada detail implementasi (aturan validasi yang ditulis langsung di dalam method), bukan pada abstraksi. Hal ini membuat kode sulit dikembangkan dan diuji.

---

## Hasil Refactoring (Implementasi SOLID)

### 1. Implementasi Dependency Inversion Principle (DIP)
Refactoring dilakukan dengan membuat abstraksi berupa interface `ILeaveValidationRule` sebagai kontrak untuk semua aturan validasi. Kelas `LeaveApprovalService` sebagai modul high-level hanya bergantung pada abstraksi tersebut, bukan pada implementasi konkret.

Dependency Injection diterapkan dengan menyuntikkan daftar aturan validasi melalui constructor.

---

### 2. Implementasi Open/Closed Principle (OCP)
Setiap aturan validasi diimplementasikan dalam class terpisah seperti:
- `LeaveDaysRule`
- `LeaveQuotaRule`

Penambahan aturan baru dapat dilakukan dengan membuat class baru yang mengimplementasikan `ILeaveValidationRule` tanpa mengubah kode `LeaveApprovalService`.

---

### 3. Implementasi Single Responsibility Principle (SRP)
Setelah refactoring, setiap class memiliki satu tanggung jawab tunggal:
- Class rule bertanggung jawab atas satu jenis validasi
- Class `LeaveApprovalService` hanya mengoordinasikan proses validasi
- Class model hanya menyimpan data

Hal ini membuat struktur kode lebih modular, jelas, dan mudah dirawat.

---

## Challenge – Pembuktian Open/Closed Principle
Sebagai pembuktian OCP, ditambahkan aturan validasi baru `EmployeeNameRule` tanpa melakukan perubahan pada kelas `LeaveApprovalService`. Sistem tetap berjalan dengan baik, yang menunjukkan bahwa desain telah terbuka untuk ekstensi namun tertutup untuk modifikasi.

---


