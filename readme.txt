                                               ,gg,                                          ,gggggggggggggg                
                                              i8""8i                                  ,dPYb,dP""""""88""""""                
                                              `8,,8'                                  IP'`YbYb,_    88                      
                                               `88'                                   I8  8I `""    88    gg                
                                               dP"8,                                  I8  8'     ggg88gggg""                
                                              dP' `8a   ,ggg,,ggg,,ggg,     ,ggggg,   I8 dP         88   8gg    ,ggg,,ggg,  
                                             dP'   `Yb ,8" "8P" "8P" "8,   dP"  "Y8gggI8dP          88    88   ,8" "8P" "8, 
                                         _ ,dP'     I8 I8   8I   8I   8I  i8'    ,8I  I8P     gg,   88    88   I8   8I   8I 
                                         "888,,____,dP,dP   8I   8I   Yb,,d8,   ,d8' ,d8b,_    "Yb,,8P  _,88,_,dP   8I   Yb,
                                         a8P"Y88888P" 8P'   8I   8I   `Y8P"Y8888P"   8P'"Y88     "Y8P'  8P""Y88P'   8I   `Y8                                                                    
===========================================================================================================================================================
      							       Selamat datang di SmolFin!===========================================================================================================================================================

SmolFin adalah sebuah aplikasi sederhana untuk mencatat dan menganalisis pengeluaran pribadi. Dengan menggunakan SmolFin, Anda dapat dengan mudah mencatat pengeluaran harian, menganalisis laporan keuangan, dan melihat tren pengeluaran Anda dalam periode tertentu.

Fitur Utama:
- Memasukkan pengeluaran harian dengan memasukkan jumlah pengeluaran dan tujuan pengeluaran.
- Menampilkan laporan keuangan dan tren pengeluaran berdasarkan rentang tanggal yang ditentukan.
- Mengedit, menghapus, mencari, dan mengekspor data pengeluaran.
- Menyimpan data pengeluaran dalam file CSV.
- Antarmuka pengguna yang sederhana dan mudah digunakan.

===========================================================================================================================================================
      								Cara Menggunakan SmolFin
===========================================================================================================================================================

1. Jalankan file smolfin.exe untuk memulai aplikasi.
2. Pilih operasi yang ingin Anda lakukan:
   - Masukkan data: Memasukkan pengeluaran harian.
   - Mengedit data: Mengubah data pengeluaran yang sudah ada.
   - Hapus data: Menghapus data pengeluaran.
   - Analisis data: Menampilkan laporan keuangan dan tren pengeluaran.
   - Lihat semua data: Menampilkan semua data pengeluaran.
   - Cari data: Mencari data pengeluaran berdasarkan kriteria tertentu.
   - Ekspor data: Menyimpan data pengeluaran dalam file CSV atau Excel.
3. Ikuti petunjuk yang diberikan dalam setiap operasi.
4. Anda dapat melanjutkan atau menghentikan operasi setelah setiap langkah.
5. Setelah selesai, aplikasi akan menutup.

===========================================================================================================================================================
								Panduan Penginstallan Ulang
===========================================================================================================================================================
Jika Anda ingin menginstall ulang, mungkin karena terjadi sebuah error, ikuti panduan ini:
1. Hapus semua file, kecuali app.py
2. Install Python versi terbaru
3. Buka cmd, atau sejenisnya, lalu ketikkan kode-kode ini satu per satu, langkah ini untuk menginstall kembali modul yang digunakan dalam app.py
   - pip install pandas
   - pip install matplotlib
   - pip install pyinstaller
4. Ubah app.py ke .exe lagi, dengan mengetikkan perintah ini di cmd: 
   - cd [direktori file]
   - pyinstaller app.py --onefile
5. Tunggu hingga SmolFin terinstall kembali
===========================================================================================================================================================
							Panduan Mengedit File 'data.csv' Secara Manual
===========================================================================================================================================================

1. Buka file CSV:
- Pastikan Anda memiliki aplikasi pengedit teks yang dapat membuka file CSV, seperti Microsoft Excel, Google Sheets, atau Notepad.
- Navigasilah ke direktori di mana file CSV disimpan.

2. Struktur file CSV:
- File CSV terdiri dari baris dan kolom.
- Setiap baris mewakili entri data tunggal.
- Setiap kolom memuat nilai atau atribut tertentu terkait entri data.

3. Struktur kolom di file 'data.csv':
- Tanggal, berisi tanggal ketika data tersebut diisi, formatnya adalah YYYY-MM-DD
- Jumlah pengeluaran, berisi jumlah pengeluaran data tersebut
- Tujuan, merupakan tujuan dari pengeluaran data tersebut

4. Mengedit nilai dalam file CSV:
- Cari entri data yang ingin Anda edit.
- Perhatikan posisi kolom dari nilai yang ingin diubah.
- Ubah nilai tersebut sesuai kebutuhan.
- Pastikan Anda tidak mengubah format file CSV (misalnya, tidak menghapus atau menambahkan tanda koma secara sembarangan), karena dapat menyebabkan kesalahan pembacaan data oleh program.

5. Menambahkan entri baru dalam file CSV:
- Buka file CSV menggunakan aplikasi pengedit teks.
- Pindahkan kursor ke baris terakhir yang berisi data.
- Buat entri data baru dengan menambahkan nilai dalam kolom yang sesuai, dipisahkan oleh tanda koma.
- Pastikan format file CSV tetap terjaga.
- Menghapus entri dalam file CSV:

6. Cari entri data yang ingin dihapus.
- Hapus baris yang berisi entri data tersebut.
- Pastikan tidak ada baris kosong yang tertinggal di antara entri data yang ada.

6. Menyimpan perubahan:
- Setelah selesai mengedit file CSV, simpan perubahan yang telah Anda buat.
- Tutup aplikasi pengedit teks.
- Pastikan Anda berhati-hati saat mengedit file CSV secara manual untuk memastikan integritas data tetap terjaga. Sebelum mengedit file CSV, disarankan - untuk membuat salinan cadangan sebagai langkah pencegahan jika terjadi kesalahan saat pengeditan.

===========================================================================================================================================================
    							 Terima kasih telah menggunakan SmolFin!
								  Developed by: Hasbi
							E-mail contact: mhasbishiddiq03@gmail.com
===========================================================================================================================================================