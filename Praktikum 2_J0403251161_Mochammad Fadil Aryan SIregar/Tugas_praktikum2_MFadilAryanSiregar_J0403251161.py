# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Mochammad Fadil Aryan Siregar
# NIM : J0403251161
# Kelas : TPL A1
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
NAMA_FILE = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(NAMA_FILE):
    stok_dict = {}
    with open(NAMA_FILE,"r",encoding="utf-8") as file:
        for stok in file:
            stok = stok.strip()
            kode,nama,stok = stok.split(",")
            stok_dict[kode] = {"kode": kode,"nama": nama,"stok": int(stok)}
        return stok_dict

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(NAMA_FILE, stok_dict):
    with open(NAMA_FILE,"w",encoding="utf-8") as file:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    print("========= DAFTAR STOK ==========")
    print(f"{"KODE":<10} | {"NAMA":<10} |{"STOK":>5}")
    print("-"*33)
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        if stok == 0:
            stok = "Stok habis"
        print(f"{kode:<10} | {nama:<10} | {stok:>5}")

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    kode_cari = input("Masukkan kode barang: ").strip()

    if kode_cari in stok_dict:
        nama = stok_dict[kode_cari]["nama"]
        stok = stok_dict[kode_cari]["stok"]
        print("==== Data Barang Ditemukan ====")
        print(f"Kode : {kode_cari}")
        print(f"Nama : {nama}")
        print(f"Stok : {stok}")

    else :
        print("MAAF BARANG TIDAK DITEMUKAN ! ")


# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    kode_input = input("Masukkan kode barang baru: ").strip()
    if kode_input in stok_dict:
        print("Kode sudah digunakan sorry bosku")
        return
    nama = input("Masukkan nama barang: ").strip()
    stok = int(input("Masukkan stok awal: ").strip())
    
    stok_dict[kode_input] = {"kode": kode_input,"nama": nama,"stok": stok} #kode ini biar data yg kita input masuk kedalam dictionarynya
    print("Data barang sudah dimasukkan. ! silahkan simpan terlebih dahulu agar barang tidak hilang yessir !")


# # -------------------------------
# # Fungsi: Update stok barang
# # -------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    if kode not in stok_dict:
        print("Maaf kode barang tidak ditemukan !")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = int(input("Masukkan pilihan (1/2): ").strip())
    if pilihan == 1:
        jml = int(input("Masukkan jumlah yang ingin ditambahkan : ").strip())
        stok_dict[kode]["stok"] += jml
        print(f"Stok sudah ditambah dari {stok_dict[kode]['stok'] - jml} menjadi {stok_dict[kode]['stok']}")

    elif pilihan == 2:
        jml = int(input("Masukkan jumlah yang ingin dikurangi : ").strip())
        stok_dict[kode]["stok"] -= jml
        print(f"stok berkurang dari {stok_dict[kode]['stok'] + jml} menjadi {stok_dict[kode]['stok']}")
        if stok_dict[kode]["stok"] < 0:
            print("Maaf angka harus bilangan real...")
            print("<<update dibatalkan>>")

# # -------------------------------
# # Program Utama
# # -------------------------------
def main():
# Membaca data dari file saat program mulai
    stok_barang = baca_stok(NAMA_FILE)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        pilihan = input("Pilih menu (jika ingin simpan ketik : save/5) : ").strip()
        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "save" or pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()