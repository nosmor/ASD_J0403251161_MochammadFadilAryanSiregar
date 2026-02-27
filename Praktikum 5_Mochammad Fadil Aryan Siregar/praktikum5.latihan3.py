# ==========================================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM  : J0403251161
# Kelas: TPL A1
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================
def cari_maks(data, index=0):
 # Base case
 # Penjelasan : Dilakukan sebagai batasan, sistemnya dalah membandingkan index dengan len(data) - 1. len(data)-1 itu menggambarkan index paling terakhird dalam data.
 # Ketika index == index paling terakhir. Akan menghasilkan elemen terbesar dalam data
    if index == len(data) - 1:
        return data[index]
 # Recursive case
 # Maks sisa untuk memasukan masing2 elemen dalam data
    maks_sisa = cari_maks(data, index + 1)
 # Di fungsi bawah ini, index paling kecil akan dibandingkan dengan maks_sisa. maks_sisa akan terjadi dimana index + 1 akan dibandingkan dengan maks_sisa lagi (index +2) dst.
 # di masing-masing rekursif pasti akan ada pemenang (angka paling besar), ketika sudah ketauan angka paling besarnya di masing-masing rekursif, maka
 # maks_sisa yang pemenang akan dibandingkan dengan data[index]. kalau salah satunya lebih besar, maka akan dikeluarkan outpunya.
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))