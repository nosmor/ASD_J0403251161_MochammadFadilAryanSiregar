# ==========================================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM  : J0403251161
# Kelas: TPL A1
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================
def biner_batas(n, batas, hasil="", jumlah_1=0):
 # Pruning: jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas:
        return
    # Base case
    if len(hasil) == n:
        print(hasil)
        return
    # Pilih '0'
    biner_batas(n, batas, hasil + "0", jumlah_1)
    # Pilih '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)
biner_batas(4, 2)

#penjelasan :
# parameter n untuk panjang baris dan batas untuk membatasi kombinasi angka 1. Ketika di run
# Fungsi akan mencari setiap komnbinasi angka sesuai dengan apa yang diinput. ketika batas sesuai dengan
# pruning, fungsi akan otomatis berhenti dan lanjut ke perhitungan selanjutnya.