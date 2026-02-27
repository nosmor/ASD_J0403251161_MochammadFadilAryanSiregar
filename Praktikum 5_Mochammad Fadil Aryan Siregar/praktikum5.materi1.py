# ==========================================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM  : J0403251161
# Kelas: TPL A1
# Contoh Rekursi 1: Faktorial
# ==========================================================
def faktorial(n):
 #jwb: Fungsi dibawah ini agar ketika fungsi rekursifnya sedang berjalan, perhitungan akan berhenti ketika angka yang terus berkurang (dari faktorial(n-1)) == 0, fungsi akan menghasilkan outputnya
    if n == 0:
        return 1 #return 1 agar output fungsi ini sama dengan output aslinya karena di kali 1.
# Fungsi rekursifnya dimana ketika memasukkan input n kedalam fungsi akan dikalikan dengan output fungsi faktorial(n-1). input akan terus mengecil hingga sama dengan (sesuai dengan base case). setelah itu fungsi selesai dan mengeluarkan output
    return n * faktorial(n - 1)
print(faktorial(5)) # Output: 120