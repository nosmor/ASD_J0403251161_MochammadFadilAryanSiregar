#  =========================================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM  : J0403251161
# Kelas: TPL A1
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================
def jumlah_list(data, index=0):
 # Base case: jika index sudah mencapai panjang list
    if index == len(data):
        return 0
    # Recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index + 1)
print(jumlah_list([2, 4, 6, 8])) # Output: 20


# penjelasan :
# ketika kita menginput data (berupa list yang berisiinteger), masing2 index akan di cek dan diinputkan ke fungsi 
# rekursifnya (return data[index] + jumlah_list(data, index + 1)) serta diproses. setelah diproses hingga index paling 
# akhir dan sesuai dengan base casenya, fungsi akan menghasilkan outputnya. Note : base case menggunakan return 0 agar ketika
# output sudah keluar, angka tidak akan di tambah data yang disimpan (di return-nya).
