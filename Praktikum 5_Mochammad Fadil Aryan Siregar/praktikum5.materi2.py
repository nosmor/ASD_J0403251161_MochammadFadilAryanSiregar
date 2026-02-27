# ==========================================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM  : J0403251161
# Kelas: TPL A1
# Contoh Rekursi 2: Tracing Masuk/Keluar
# ==========================================================
def hitung(n):
# Base case
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n) # fase stacking
    hitung(n - 1) # pemanggilan rekursif
    print("Keluar:", n) # fase unwinding
hitung(3)

#Penjelasan :
# Ketika input dimasukkan, input awal akan disimpan pada n dan lanjut ke fungsi rekursifnya dan terjadi perhitungan yang sama lagi hingga n == 0 (sesuai base casenya) 
# dan mengeluarkan output selesai, namun karena belum semua fungsinya terjalan, dari fungsi rekursif yang paling terakhir diproses akan menjalankan fungsi
# print("keluar", n), sehingga menghasilkan fungsi yang first to enter, last to exit. polanya seperti 3 2 1 selesai 1 2 3 .