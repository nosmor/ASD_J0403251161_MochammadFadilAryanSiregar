# =========================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM : J0403251161
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# =========================================

edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

edges.sort()

mst = []           
total_weight = 0   
connected = set()  

for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

# Tampilkan hasil
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# ==========================================================
# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
#    Edge (C, D) dengan bobot 1
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Agar total bobot MST seminimal mungkin. Dengan memilih yang
#    terkecil duluan, kita memastikan tidak ada kombinasi yang lebih murah.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot = 1 + 2 + 3 = 6
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Edge (A,B)=4 dan (A,D)=5 tidak dipilih karena saat giliran
#    mereka diperiksa, semua node (A,B,C,D) sudah terhubung,
#    sehingga menambahkannya akan membentuk cycle.
# ==========================================================