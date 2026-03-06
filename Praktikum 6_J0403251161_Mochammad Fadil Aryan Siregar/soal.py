# --------------------------------------
# Nama : Mochammad Fadil Aryan Siregar
# Kelas : TPL A1
# NIM : J0403251161
# --------------------------------------

def perhitungan(nilai):
    exchanges = True
    passnum = len(nilai)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if nilai[i] < nilai[i+1]:
                exchanges = True
                temp = nilai[i]
                nilai[i] = nilai[i+1]
                nilai[i+1] = temp
        passnum = passnum-1


nilai = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
perhitungan(nilai)
print(nilai[:5])   