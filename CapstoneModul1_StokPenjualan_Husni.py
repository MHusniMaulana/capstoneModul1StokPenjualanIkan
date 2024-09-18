# Program CRUD
def main():
    while True:
        print("\nMenu CRUD:")
        print("1. Tampilkan Stok")
        print("2. Tambah Stok")
        print("3. Update Stok")
        print("4. Hapus Stok")
        print("5. Hitung Profitabilitas") # menu tambahan yg masukan kedalam program sebagai penambah nilai
        print("6. Keluar")
        
        pilihan = input("Masukkan pilihan (1-6): ")
        
        if pilihan == "1":
            tampilkan_stok(stok_penjualan)
        elif pilihan == "2":
            tambah_stok(stok_penjualan)
        elif pilihan == "3":
            update_stok(stok_penjualan)
        elif pilihan == "4":
            hapus_stok(stok_penjualan)
        elif pilihan == "5":
            hitung_profitabilitas(stok_penjualan)
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Data Stok Penjualan Awal
stok_penjualan = [
    {"asal": "Ambon", "jenis_ikan": "Platinum", "jumlah_ikan": 10, "harga_beli": 70000, "harga_jual": 100000},
    {"asal": "Ambon", "jenis_ikan": "Black Storm", "jumlah_ikan": 3, "harga_beli": 400000, "harga_jual": 488000},
]

# Fungsi Create (Menambahkan Data Baru)
def tambah_stok(stok):
    asal = input("Masukkan asal ikan: ")
    jenis_ikan = input("Masukkan jenis ikan: ")
    jumlah_ikan = int(input("Masukkan jumlah ikan: "))
    harga_beli = int(input("Masukkan harga beli (Rp): "))
    harga_jual = int(input("Masukkan harga jual (Rp): "))
    
    stok_baru = {"asal": asal, "jenis_ikan": jenis_ikan, "jumlah_ikan": jumlah_ikan, "harga_beli": harga_beli, "harga_jual": harga_jual}
    stok.append(stok_baru)
    print(f"Data ikan {jenis_ikan} berhasil ditambahkan!")

# Fungsi Read (Menampilkan Data)
def tampilkan_stok(stok):
    print("{:<10} {:<20} {:<15} {:<15} {:<15}".format("Asal", "Jenis Ikan", "Jumlah Ikan", "Harga Beli", "Harga Jual"))
    print("-" * 70)
    for s in stok:
        print("{:<10} {:<20} {:<15} Rp{:<15} Rp{:<15}".format(s["asal"], s["jenis_ikan"], s["jumlah_ikan"], s["harga_beli"], s["harga_jual"]))

# Fungsi Update (Memperbarui Data)
def update_stok(stok):
    jenis_ikan = input("Masukkan jenis ikan yang ingin diperbarui: ")
    field = input("Field yang ingin diperbarui (asal/jumlah_ikan/harga_beli/harga_jual): ")
    nilai_baru = input("Masukkan nilai baru: ")
    
    for s in stok:
        if s["jenis_ikan"] == jenis_ikan:
            if field == "jumlah_ikan" or field == "harga_beli" or field == "harga_jual":
                nilai_baru = int(nilai_baru)  # Konversi menjadi integer jika nilai baru adalah angka
            s[field] = nilai_baru
            print(f"Data ikan {jenis_ikan} berhasil diperbarui!")
            return
    print(f"Jenis ikan {jenis_ikan} tidak ditemukan!")

# Fungsi Delete (Menghapus Data)
def hapus_stok(stok):
    jenis_ikan = input("Masukkan jenis ikan yang ingin dihapus: ")
    
    for s in stok:
        if s["jenis_ikan"] == jenis_ikan:
            stok.remove(s)
            print(f"Data ikan {jenis_ikan} berhasil dihapus!")
            return
    print(f"Jenis ikan {jenis_ikan} tidak ditemukan!")

# Fungsi Analisis Profitabilitas
def hitung_profitabilitas(stok):
    total_profit = 0
    print("Analisis Profitabilitas:")
    print("="*50)
    print("{:<20} {:<15} {:<15} {:<15}".format("Jenis Ikan", "Keuntungan", "Margin (%)", "Keuntungan Total"))
    print("-"*50)
    
    for s in stok:
        keuntungan_per_unit = s["harga_jual"] - s["harga_beli"]
        keuntungan_total = keuntungan_per_unit * s["jumlah_ikan"]
        margin_keuntungan = (keuntungan_per_unit / s["harga_beli"]) * 100
        
        print("{:<20} Rp{:<14} {:<14.2f}% Rp{:<15}".format(
            s["jenis_ikan"], keuntungan_per_unit, margin_keuntungan, keuntungan_total))
        
        total_profit += keuntungan_total
    
    print("-"*50)
    print(f"Total Keuntungan Keseluruhan: Rp{total_profit}")

# Menjalankan program
main()
