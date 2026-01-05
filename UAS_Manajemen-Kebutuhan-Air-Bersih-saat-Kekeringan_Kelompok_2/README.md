# Sistem Manajemen Air Bersih (Water Management System)

Aplikasi CLI untuk mengelola distribusi air bersih melalui armada truk tangki. Sistem ini dirancang untuk membantu posko kekeringan dalam mengkoordinasikan pendistribusian air ke masyarakat.

## 📋 Deskripsi

Aplikasi ini adalah sistem manajemen air bersih yang memungkinkan pengguna untuk:
- Mendaftarkan armada truk tangki air
- Melakukan pengisian ulang air ke truk
- Mendistribusikan/mengurangi air dari truk
- Memantau status ketersediaan air secara real-time
- Menyimpan data secara persisten ke file JSON

Data truk dan status air disimpan secara otomatis ke file `data_truk.json`, sehingga informasi tidak hilang saat aplikasi ditutup.

## ✨ Fitur Utama

1. **Manajemen Armada Truk**
   - Pendaftaran truk tangki baru dengan ID, plat nomor, dan kapasitas
   - Penyimpanan data otomatis ke file JSON

2. **Pengisian Air**
   - Pengisian ulang air ke truk dengan validasi kapasitas maksimum
   - Logging timestamp setiap transaksi

3. **Distribusi Air**
   - Pengurangan stok air untuk distribusi ke warga
   - Validasi ketersediaan stok sebelum distribusi
   - Feedback real-time untuk setiap operasi

4. **Monitoring Status**
   - Pengecekan status semua truk terdaftar
   - Informasi stok air dan kapasitas maksimum

5. **Persistensi Data**
   - Auto-save ke file JSON setiap ada perubahan
   - Auto-load data saat aplikasi dimulai
   - Format JSON yang mudah dibaca dan diedit

## 🏗️ Struktur Project

```
uas_watermanagement_kelompok_2/
│
├── main.py                      # Entry point aplikasi
├── data_truk.json              # File penyimpanan data (auto-generated)
├── README.md                   # Dokumentasi project
│
├── models/                     # Layer Model (Entity)
│   ├── __init__.py
│   ├── base_model.py          # Abstract class Identifiable
│   └── entities.py            # Class SumberAir & TrukTangki
│
├── repositories/              # Layer Data Access
│   ├── __init__.py
│   ├── base_repository.py    # Abstract repository interface
│   ├── memory_repository.py  # In-memory storage
│   └── file_repository.py    # JSON file storage
│
├── services/                  # Layer Business Logic
│   ├── __init__.py
│   └── water_service.py      # WaterDistributionService
│
└── utils/                     # Utilities
    ├── __init__.py
    └── logger.py             # Logging configuration
```

## 🎯 Konsep OOP yang Diterapkan

### 1. **Abstraction**
- `Identifiable` (abstract class) - Mendefinisikan kontrak untuk objek yang dapat diidentifikasi
- `BaseRepository` (abstract class) - Mendefinisikan interface untuk data persistence

### 2. **Inheritance**
- `SumberAir` extends `Identifiable`
- `TrukTangki` extends `SumberAir`
- `FileRepository` implements `BaseRepository`

### 3. **Encapsulation**
- Private attribute `__stok_air` dengan getter/setter untuk validasi
- Protected attribute `_uid` dan `_kapasitas_max`

### 4. **Polymorphism**
- Method `info()` di-override di `SumberAir` dan `TrukTangki`
- Setiap class memberikan implementasi spesifik

### 5. **Dependency Injection**
- `WaterDistributionService` menerima `BaseRepository` melalui constructor
- Memungkinkan loose coupling dan mudah untuk testing

## 🛠️ Teknologi yang Digunakan

- **Python 3.x** - Bahasa pemrograman utama
- **JSON** - Format penyimpanan data
- **Logging** - Untuk tracking aktivitas sistem
- **ABC (Abstract Base Classes)** - Untuk abstraction dan interface

## 📦 Instalasi

1. **Clone atau download project ini**
   ```bash
   git clone <repository-url>
   cd uas_watermanagement_kelompok_2
   ```

2. **Pastikan Python 3.x terinstall**
   ```bash
   python --version
   ```

3. **Tidak ada dependencies eksternal** - Project ini hanya menggunakan library bawaan Python

## 🚀 Cara Menggunakan

1. **Jalankan aplikasi**
   ```bash
   python main.py
   ```

2. **Menu Utama**
   ```
   === MENU POSKO KEKERINGAN ===
   1. Tambah Armada Truk Air
   2. Isi Ulang Air
   3. Gunakan Air dari Truk
   4. Cek Status Air
   5. Keluar
   ```

3. **Contoh Penggunaan**

   **Menambah Truk Baru:**
   ```
   Pilih menu: 1
   ID Truk: T001
   Plat Nomor: B1234XYZ
   Kapasitas (Liter): 5000
   ```

   **Mengisi Ulang Air:**
   ```
   Pilih menu: 2
   ID Truk yang diisi: T001
   Jumlah Air (Liter): 3000
   ```

   **Mendistribusikan Air:**
   ```
   Pilih menu: 3
   ID Truk yang akan digunakan: T001
   Jumlah Air yang akan digunakan (Liter): 500
   ```

   **Cek Status:**
   ```
   Pilih menu: 4
   
   --- STATUS KETERSEDIAAN AIR ---
   [TRUK B1234XYZ] Sumber Air di Mobil | Stok: 2500/5000 L
   ```

## 📊 Format Data JSON

Data disimpan dalam file `data_truk.json` dengan format:

```json
[
    {
        "type": "TrukTangki",
        "uid": "T001",
        "plat_nomor": "B1234XYZ",
        "kapasitas_max": 5000.0,
        "stok_air": 2500.0
    }
]
```

## 🔍 Detail Implementasi

### Models Layer
- **Identifiable**: Abstract base class untuk semua objek yang memerlukan ID unik
- **SumberAir**: Representasi sumber air dengan enkapsulasi stok air
- **TrukTangki**: Spesialisasi dari SumberAir untuk truk tangki

### Repository Layer
- **BaseRepository**: Interface untuk operasi CRUD
- **FileRepository**: Implementasi dengan persistensi ke JSON file
  - Auto-save setiap perubahan
  - Auto-load saat inisialisasi
  - Error handling untuk file corrupt

### Service Layer
- **WaterDistributionService**: Business logic untuk:
  - Pendaftaran sumber air
  - Pengisian dan pengurangan air
  - Monitoring status
  - Validasi operasi

### Utils Layer
- **Logger**: Konfigurasi logging untuk tracking aktivitas sistem

## 📝 Validasi dan Error Handling

1. **Validasi Stok Air**
   - Stok tidak boleh negatif
   - Stok tidak boleh melebihi kapasitas maksimum

2. **Validasi Distribusi**
   - Memastikan stok mencukupi sebelum pengurangan
   - Menampilkan error jika stok tidak cukup

3. **File Handling**
   - Membuat file baru jika belum ada
   - Handling untuk file corrupt atau format invalid
   - Logging setiap operasi file

## 🔧 Logging

Semua aktivitas dicatat dalam log dengan format:
```
2025-12-30 10:30:45 - INFO - Aplikasi Manajemen Air Bersih Dimulai...
2025-12-30 10:31:20 - INFO - Sumber air T001 berhasil didaftarkan.
2025-12-30 10:32:15 - INFO - Isi ulang 3000L ke T001 berhasil. Waktu: 2025-12-30 10:32:15
```

## 📄 Lisensi

Project ini dibuat untuk keperluan pembelajaran dan dapat digunakan secara bebas.

## 👨‍💻 Pengembang

**Kelompok 2 - UAS Water Management**

1. Andi Reza - 2411102441164
2. Alan Yahya - 2411102441162
3. Rafa Haris - 2411102441049
4. Malik Sabarullah Akbar -2411102441250 
5. Muhammad Ishaq -2411102441191
6. Fahryandy Adithia -2411102441046
7. Muhammad Fahbian Alzi Annur-2411102441241

---

**Dibuat dengan ❤️ untuk membantu distribusi air bersih yang lebih efisien**
