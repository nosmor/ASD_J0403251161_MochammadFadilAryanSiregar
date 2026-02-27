# ==========================================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM  : J0403251161
# Kelas: TPL A1
# Latihan 4: Kombinasi Huruf
# ==========================================================
def kombinasi(n, hasil=""):
    #Base case
    if len(hasil) == n:
        print(hasil)
        return
    
    # Ketika batasan dimasukkan (n), fungsi akan otomatis masuk ke rekursif ini hingga ketemu setiap kombinasinya sepanjang batas yang dimasukkan.
    # Fungsi melakukan eksploring, sehingga memungkinkan untuk melakukan kombinasi antara A dan B
    # Choose + explore = tambah 'A'
    kombinasi(n, hasil + "A")
    # Choose + explore = tambah 'B'
    kombinasi(n, hasil + "B")
kombinasi(2)

