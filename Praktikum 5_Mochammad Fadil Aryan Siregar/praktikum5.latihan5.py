# ==========================================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM  : J0403251161
# Kelas: TPL A1
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    # Base Case:
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    # Fungsi rekursifnya disini, fungsi akan mencoba eksplor untuk mencari kombinasi angka sepanjang input yg dimasukkan.
    for angka in ["0", "1", "2"]:
        if angka not in hasil: # agar angka yang sama tidak muncul bersamaan, fungsi ini untuk membandingkan jika angka didalam string ada angka yang sama atau tidak, jika tidak maka akan lanjut rekursifnya.
            buat_pin(panjang, hasil + angka) 
# Sehingga output yang keluar adalah string yang tidak mengandung angka yang sama.
buat_pin(3)