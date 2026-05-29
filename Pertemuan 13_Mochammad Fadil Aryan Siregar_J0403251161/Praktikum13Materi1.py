# =========================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM : J0403251161
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# =========================================

# ==========================================================
# Implementasi Kruskal
# ==========================================================

# Daftar edge dalam format (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),   # edge C-D dengan bobot 1
    (2, 'A', 'C'),   # edge A-C dengan bobot 2
    (3, 'B', 'D'),   # edge B-D dengan bobot 3
    (4, 'A', 'B'),   # edge A-B dengan bobot 4
    (5, 'A', 'D')    # edge A-D dengan bobot 5
]

# Urutkan semua edge dari bobot terkecil ke terbesar
edges.sort()

mst = []           # list untuk menyimpan edge yang masuk MST
total_weight = 0   # akumulasi total bobot MST
connected = set()  # set node yang sudah terhubung dalam MST

# Periksa satu per satu edge yang sudah diurutkan
for weight, u, v in edges:
    # Tambahkan edge hanya jika salah satu node-nya belum terhubung
    # (mencegah terbentuknya cycle secara sederhana)
    if u not in connected or v not in connected:
        mst.append((u, v, weight))   # simpan edge ke MST
        total_weight += weight        # tambahkan bobot ke total
        connected.add(u)             # tandai node u sudah terhubung
        connected.add(v)             # tandai node v sudah terhubung

# Tampilkan hasil MST
print("Minimum Spanning Tree (Kruskal):")
for edge in mst:
    print(f"  {edge[0]} - {edge[1]}, bobot = {edge[2]}")

print("Total bobot =", total_weight)