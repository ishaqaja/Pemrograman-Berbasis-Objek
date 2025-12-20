# DEBUG REPORT – Bug PPN 10%

## Deskripsi Bug
Ditemukan bug pada fungsi `hitung_diskon` di file `diskon_service.py` di mana PPN 10% dihitung dua kali sehingga menyebabkan harga akhir menjadi lebih besar dari seharusnya.

## Langkah Debugging Menggunakan pdb
Debugging dilakukan dengan menambahkan perintah `pdb.set_trace()` di dalam fungsi `hitung_diskon`. Program kemudian dijalankan sehingga eksekusi berhenti pada titik tersebut dan dapat ditelusuri baris per baris menggunakan debugger pdb.

## Penelusuran Variabel
Saat proses debugging, dilakukan pengecekan nilai variabel menggunakan perintah `p` pada pdb dengan hasil sebagai berikut:

- `p harga_setelah_diskon`  
  Menunjukkan harga setelah diskon sudah benar.

- `p ppn`  
  Menunjukkan nilai PPN sebesar 10% dari harga setelah diskon.

- `p harga_setelah_ppn`  
  Menunjukkan bahwa nilai PPN ditambahkan dua kali ke harga setelah diskon.

Hasil pengecekan ini membuktikan bahwa variabel `ppn` digunakan lebih dari satu kali dalam perhitungan harga akhir.

## Akar Masalah
Akar masalah bug adalah adanya dua baris penambahan PPN pada harga setelah diskon, yaitu PPN 10% ditambahkan dua kali secara tidak sengaja.

## Perbaikan
Perbaikan dilakukan dengan menghapus penambahan PPN yang kedua sehingga PPN hanya dihitung dan ditambahkan satu kali ke harga setelah diskon. Setelah perbaikan, fungsi hanya menghitung diskon sesuai kebutuhan pengujian.

## Kesimpulan
Bug berhasil diidentifikasi menggunakan pdb melalui pengecekan nilai variabel, dan setelah dilakukan perbaikan, perhitungan harga akhir berjalan dengan benar serta seluruh unit test berhasil dijalankan.
