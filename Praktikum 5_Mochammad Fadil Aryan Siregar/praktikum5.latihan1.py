# ==========================================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM  : J0403251161
# Kelas: TPL A1
# Latihan 1: Rekursi Pangkat
# ==========================================================
def pangkat(a, n):
 # Base case
 # Penjelasan : Fungsi ini akan menjadi batasan agar fungsi rekursif tidak terus mengurang dan melakukan perhitungan yang tak terbatas.
    if n == 0:
        return 1
 # Recursive case
 # Penjelasan : dalam kasus ini, recursive casenya untuk melakukan perhitungan terulang sebanyak n kali. perhitungan yang dilakukan adalah perkalian dengan a,
 # Ketika a dan n dimasukkan, n akan menyesuaikan dulu dengan base case, ketika tidak sama dengan 0 maka perhitungan akan lanjut ke rekursifnya.
 # return a * pangkat(a, n - 1). a akan dikali dengan a sebanyak n kali karena (n-1). n akan terus berkurang hingga sama engan base case.
    return a * pangkat(a, n - 1)
print(pangkat(2, 4)) # Output: 16
