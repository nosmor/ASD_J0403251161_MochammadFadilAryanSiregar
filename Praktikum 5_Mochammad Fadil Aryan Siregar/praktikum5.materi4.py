# ==========================================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM  : J0403251161
# Kelas: TPL A1
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================
def biner(n, hasil=""):
 # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    # Choose + Explore: tambah '0'
    biner(n, hasil + "0")
    # Choose + Explore: tambah '1'
    biner(n, hasil + "1")
biner(3)

#penjelasan: 
# Input yang dimasukkan akan menjadi panjang bilangan biner. ketika dimasukkan n, akan terproses oleh biner(n, hasil="0") dengan panjang n dan mengeluarkan nilai (karena return)
# Kemudian fungsi akan lanjut eksplorasi kalau ditambah 1 (biner(n, hasil + "1")). Hasilnya akan mengeluarkan semua kombinasi angka dengan panjang n.