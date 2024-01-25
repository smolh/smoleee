import csv
from datetime import date, timedelta
import pandas as pd
import matplotlib.pyplot as plt
from time import sleep
import os

def inputdata():
    # Mengambil input pengeluaran dari sistem
    try:
        pengeluaran = int(input("Masukkan pengeluaran hari ini: "))
    except ValueError:
        print('Input tidak valid, masukkan angka saja')
        return
    
    tujuan = input('Masukkan tujuan pengeluaran uang,\nj = jajan\nk = kas\no = lainnya\nmasukkan input: ')
    tujuan_convert = ''

    # Menyingkronkan data
    if tujuan.lower() == 'j':
        tujuan_convert = 'jajan'
    elif tujuan.lower() == 'o':
        tujuan_convert = 'lainnya'
    elif tujuan.lower() == 'k':
        tujuan_convert = 'kas'
    else:
        print('Input tidak valid, cukup masukkan j, k, atau o saja')
        return

    print(f'Data disimpan: {pengeluaran} untuk {tujuan_convert}')

    # Mendapatkan tanggal saat ini
    current_date = date.today().strftime("%Y-%m-%d")

    # Mengecek keberadaan file CSV
    if not os.path.isfile('data.csv'):
        # Jika file tidak ada, membuat file baru dengan header
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['tanggal', 'jumlah pengeluaran', 'tujuan'])

    # Membaca data CSV
    df = pd.read_csv('data.csv')

    # Mengkonversi kolom 'tanggal' menjadi tipe datetime
    df['tanggal'] = pd.to_datetime(df['tanggal'])

    # Tentukan rentang tanggal yang ingin diisi
    start_date = df['tanggal'].max() + timedelta(days=1) if not df.empty else current_date
    end_date = current_date

   # Periksa dan tambahkan entri baru jika tanggal tidak ada dalam data CSV
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    missing_dates = list(set(date_range) - set(df['tanggal']))

    missing_data = pd.DataFrame({'tanggal': missing_dates, 'jumlah pengeluaran': 0, 'tujuan': 'tidak ada pengeluaran hari ini'})
    missing_data['tanggal'] = pd.to_datetime(missing_data['tanggal']).dt.date
    missing_data = missing_data.sort_values('tanggal')
    missing_data['tanggal'] = pd.to_datetime(missing_data['tanggal']).dt.strftime('%Y-%m-%d')

    df['tanggal'] = pd.to_datetime(df['tanggal']).dt.strftime('%Y-%m-%d')

    df = pd.concat([df, missing_data], ignore_index=True)


    # Menambahkan entri baru untuk data pengeluaran hari ini
    new_data = pd.DataFrame({'tanggal': [current_date], 'jumlah pengeluaran': [pengeluaran], 'tujuan': [tujuan_convert]})
    df = pd.concat([df, new_data], ignore_index=True)

    # Menulis data ke dalam file CSV
    df.to_csv('data.csv', index=False)


def getdata(isRanged):
    try:
        # Membaca file CSV
        df = pd.read_csv('data.csv')

        # Konversi kolom tanggal menjadi tipe data datetime
        df['tanggal'] = pd.to_datetime(df['tanggal'])

        def laporan_keuangan(start_date, end_date):
            # Filter berdasarkan range tanggal
            filtered_df = df[(df['tanggal'] >= start_date) & (df['tanggal'] <= end_date)]

            # Filter berdasarkan kategori
            kategori_pengeluaran = filtered_df.groupby('tujuan')['jumlah pengeluaran'].sum()

            # Menghitung total pengeluaran dalam periode yang ditentukan
            total_pengeluaran = filtered_df['jumlah pengeluaran'].sum()

            # Menghitung rata-rata pengeluaran
            rata_pengeluaran = filtered_df['jumlah pengeluaran'].mean()

            # Menampilkan laporan keuangan
            print(f"Laporan Keuangan ({start_date} - {end_date}):")
            print("-------------------------------")
            print(filtered_df)
            print("-------------------------------")
            print(f"Total Pengeluaran: {total_pengeluaran}")
            print(f'Rata-rata Pengeluaran Per Hari: {rata_pengeluaran}')
            print("Analisis Kategori Tujuan Pengeluaran:")
            print("--------------------------------------")
            print(kategori_pengeluaran)
            print()

        def tren_pengeluaran(start_date, end_date):
            kategori_pengeluaran = df.loc[df['tujuan'] != 'tidak ada pengeluaran hari ini'].groupby('tujuan')['jumlah pengeluaran'].sum()

            # Filter berdasarkan range tanggal
            filtered_df = df[(df['tanggal'] >= start_date) & (df['tanggal'] <= end_date)]

            # Menghitung total pengeluaran per tanggal
            daily_total = filtered_df.groupby('tanggal')['jumlah pengeluaran'].sum()

            # Plot tren pengeluaran menggunakan pyplot
            plt.plot(daily_total.index, daily_total.values)
            plt.xlabel('Tanggal', )
            plt.ylabel('Total Pengeluaran')
            plt.title('Tren Pengeluaran')
            plt.xticks(rotation=45)

            # Menampilkan diagram pie
            plt.figure(figsize=(6, 6))
            plt.pie(kategori_pengeluaran, labels=kategori_pengeluaran.index, autopct=lambda pct: f"{pct:.1f}%\n({int(pct * sum(kategori_pengeluaran) / 100)})")
            plt.title('Pengeluaran Berdasarkan Kategori')
            plt.show()

        # Input range tanggal dari pengguna
        if isRanged == True:
            start_date = input("Masukkan tanggal awal (yyyy-mm-dd): ")
            end_date = input("Masukkan tanggal akhir (yyyy-mm-dd): ")
        else:
            start_date = df.iloc[0]['tanggal']
            end_date = df.iloc[-1]['tanggal']

        # Memanggil fungsi laporan_keuangan dan tren_pengeluaran dengan range tanggal yang diberikan
        laporan_keuangan(start_date, end_date)
        tren_pengeluaran(start_date, end_date)
    except TypeError:
        print('Input error, silahkan masukkan data valid')
        return


def editdata():
    # Membaca file CSV
    df = pd.read_csv('data.csv')

    # Konversi kolom tanggal menjadi tipe data datetime
    df['tanggal'] = pd.to_datetime(df['tanggal'])

    # Menampilkan data yang dapat diedit
    print("Data yang dapat diedit:")
    print(df)
    print()

    # Meminta input nomor baris yang akan diedit
    try:
        row_num = int(input("Masukkan nomor baris yang akan diedit: "))
    except ValueError:
        print('Masukkan angka saja')
        return
    # Memeriksa apakah nomor baris valid
    if row_num < 0 or row_num >= len(df):
        print("Nomor baris tidak valid.")
        return

    # Mengambil data pada baris yang akan diedit
    row_data = df.iloc[row_num]

    # Menampilkan data yang akan diedit
    print("Data yang akan diedit:")
    print(row_data)
    print()

    # Meminta input untuk pengubahan data
    pengeluaran = input("Masukkan pengeluaran yang baru: ")
    tujuan = input('Masukkan tujuan pengeluaran yang baru (j = jajan, k = kas, o = lainnya): ')

    # Menyingkronkan data
    tujuan_convert = ''
    if tujuan.lower() == 'j':
        tujuan_convert = 'jajan'
    elif tujuan.lower() == 'o':
        tujuan_convert = 'lainnya'
    elif tujuan.lower() == 'k':
        tujuan_convert = 'kas'
    else:
        tujuan_convert = 'lainnya'

    # Memperbarui data pada baris yang dipilih
    df.at[row_num, 'jumlah pengeluaran'] = pengeluaran
    df.at[row_num, 'tujuan'] = tujuan_convert

    # Menulis data yang telah diperbarui ke file CSV
    df.to_csv('data.csv', index=False)

    print("Data berhasil diperbarui.")

def searchdata():
    # Membaca file CSV
    df = pd.read_csv('data.csv')

    # Konversi kolom tanggal menjadi tipe data datetime
    df['tanggal'] = pd.to_datetime(df['tanggal'])

    # Meminta input dari pengguna
    print("Pencarian Data:")
    print("1. Berdasarkan Pengeluaran")
    print("2. Berdasarkan Kategori")
    print("3. Berdasarkan Tanggal")
    option = input("Pilih opsi pencarian (1/2/3): ")

    if option == '1':
        # Pencarian berdasarkan pengeluaran
        min_pengeluaran = float(input("Masukkan minimal pengeluaran: "))
        max_pengeluaran = float(input("Masukkan maksimal pengeluaran: "))

        filtered_df = df[(df['jumlah pengeluaran'] >= min_pengeluaran) & (df['jumlah pengeluaran'] <= max_pengeluaran)]
    elif option == '2':
        # Pencarian berdasarkan kategori
        kategori = input("Masukkan kategori pengeluaran: ")

        filtered_df = df[df['tujuan'] == kategori]
    elif option == '3':
        # Pencarian berdasarkan tanggal
        tanggal = input("Masukkan tanggal (yyyy-mm-dd): ")

        filtered_df = df[df['tanggal'] == tanggal]
    else:
        print("Opsi pencarian tidak valid.")
        return

    # Menampilkan hasil pencarian
    if filtered_df.empty:
        print("Data tidak ditemukan.")
    else:
        print("Hasil Pencarian:")
        print(filtered_df)

def exportdata():
    # Membaca file CSV
    df = pd.read_csv('data.csv')

    file_dir = os.getcwd()
    # Meminta input dari pengguna
    filename = input("Masukkan nama file untuk ekspor data: ")
    format_option = input("Pilih format ekspor (csv/excel): ")

    if os.path.exists(f'{filename}.{format_option}'):
        print(f'File dengan nama \'{filename}.{format_option}\' telah ada, coba cari nama lain')
        return
    try:
        if format_option.lower() == 'csv':
            # Menyimpan data ke dalam file CSV
            df.to_csv(filename + '.csv', index=False)
            print("Data berhasil diekspor ke file", filename + '.csv')
        elif format_option.lower() == 'excel':
            # Menyimpan data ke dalam file Excel
            df.to_excel(filename + '.xlsx', index=False)
            print("Data berhasil diekspor ke file", filename + '.xlsx, dan disimpan dalam direktori ' + file_dir)
        else:
            print("Format ekspor tidak valid. Pilih format csv atau excel.")
    except Exception as e:
        print("Terjadi kesalahan saat melakukan ekspor data:", str(e))

def deletedata():
    # Membaca file CSV
    df = pd.read_csv('data.csv')

    # Menampilkan data yang dapat dihapus
    print("Data yang dapat dihapus:")
    print(df)
    print()

    # Meminta input nomor baris yang akan dihapus
    try:
        row_num = int(input("Masukkan nomor baris yang akan dihapus: "))
    except ValueError:
        print('Masukkan angka saja')
        return
    # Memeriksa apakah nomor baris valid
    if row_num < 0 or row_num >= len(df):
        print("Nomor baris tidak valid.")
        return

    # Mengambil data pada baris yang akan dihapus
    row_data = df.iloc[row_num]

    # Menghapus data jika ada tanggal yang sama
    if len(df[df['tanggal'] == row_data['tanggal']]) > 1:
        df = df.drop(row_num)

        # Menulis data yang telah dihapus ke file CSV
        df.to_csv('data.csv', index=False)

        print("Data berhasil dihapus.")
    else:
        # Mengganti data jika tanggal tersebut hanya satu-satunya di data frame
        df.at[row_num, 'jumlah pengeluaran'] = 0
        df.at[row_num, 'tujuan'] = 'tidak ada pengeluaran hari ini'

        # Menulis data yang telah diubah ke file CSV
        df.to_csv('data.csv', index=False)

        print("Data telah diubah menjadi tidak ada pengeluaran hari ini.")

# menu
while True:
    if not os.path.exists('data.csv'):
        print('==Selamat Datang Pengguna Baru==')
        print('Kami menyarankan untuk membuka file readme.txt, apakah kamu ingin membukanya di sini? (Kami menyarankan untuk membukanya secara langsung) (Y/N)')
        isOpenreadme = input('')
        if isOpenreadme.lower() == 'y':
            with open('readme.txt', 'r') as file:
                a = file.readlines()
                for i in a:
                    print(i)
        print('Baiklah, terima kasih!')
        header = 'tanggal,jumlah pengeluaran,tujuan\n'

        with open('data.csv', 'w') as file:
            file.write(header)

    df = pd.read_csv('data.csv')
    menu = input('''Masukkan operasi yang ingin Anda lakukan:
1. Masukkan data
2. Mengedit data
3. Hapus data
4. Analisis data
5. Lihat semua data
6. Cari data
7. Ekspor data
Masukkan nomor operasi: ''')
    if menu == '1':
        inputdata()

    elif menu== '4':
        isRanged = input('1. Semua data yang dimasukkan\n2. Tentukan range data\nMasukkan angka opsi: ')
        if isRanged == '1':
            getdata(False)
        elif isRanged == '2':
            getdata(True)
        else:
            print('INPUT INVALID')

    elif menu == '2':
        editdata()

    elif menu == '6':
        searchdata()

    elif menu == '7':
        exportdata()

    elif menu == '3':
        deletedata()

    elif menu == '5':
        print(df)

    else:
        print('INPUT INVALID')

    isContinue = input('\nApakah kamu ingin melanjutkan operasi? (Y/N) ')

    if isContinue.lower() == 'y':
        print('Memulai ulang..')
        sleep(0.5)
        os.system('cls')
    else:
        print('Menutup..')
        sleep(0.5)
        break