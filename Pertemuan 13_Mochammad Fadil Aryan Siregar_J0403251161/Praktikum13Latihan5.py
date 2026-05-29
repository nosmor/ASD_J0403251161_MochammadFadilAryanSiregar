# =========================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM : J0403251161
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# =========================================

# Representasi weighted graph jaringan jalan antar kota
edges = [
    (5, 'Bogor',   'Jakarta'),  
    (2, 'Bogor',   'Depok'),  
    (3, 'Depok',   'Jakarta'),  
    (6, 'Jakarta', 'Bandung'),  
    (4, 'Depok',   'Bandung')   
]

# Urutkan semua edge dari jarak terkecil ke terbesar
edges.sort()

mst = [] # daftar jalan yang masuk ke MST
total_weight = 0 # total jarak/biaya MST
connected = set() # set kota yang sudah terhubung

# Periksa edge satu per satu (sudah terurut dari terkecil)
for weight, u, v in edges:
    # Tambahkan jalan jika salah satu kota belum terhubung (hindari cycle)
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u) # tandai kota u sudah masuk jaringan
        connected.add(v) # tandai kota v sudah masuk jaringan

# Tampilkan hasil MST
print("MST - Jaringan Jalan Antar Kota (Kruskal):")
print("=" * 45)
for edge in mst:
    print(f"  {edge[0]} --> {edge[1]}, jarak = {edge[2]}")

print("=" * 45)
print(f"Total jarak minimum = {total_weight}")

# ==========================================================
# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
#    Kasus 1 - Jaringan Jalan Antar Kota (Bogor, Depok,
#    Jakarta, Bandung).
#
# 2. Algoritma apa yang digunakan?
#    Algoritma Kruskal. Dipilih karena data tersedia dalam
#    bentuk daftar edge, dan graph ini memiliki sedikit edge, 
#    sehingga Kruskal lebih cocok dan mudah diimplementasikan.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    Bogor  --> Depok,   jarak = 2
#    Depok  --> Jakarta, jarak = 3
#    Depok  --> Bandung, jarak = 4
#
# 4. Berapa total bobot MST?
#    2 + 3 + 4 = 9
#
# 5. Mengapa edge tertentu tidak dipilih?
#    Bogor-Jakarta (5) tidak dipilih karena Bogor dan Jakarta
#    sudah terhubung via Depok, menambahkannya akan membuat cycle.
#    Jakarta-Bandung (6) tidak dipilih karena Bandung sudah
#    terhubung via Depok, dan jalur Depok-Bandung lebih murah.
# ==========================================================