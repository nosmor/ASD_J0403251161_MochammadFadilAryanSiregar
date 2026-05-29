# =========================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM : J0403251161
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# =========================================

import heapq 

# Representasi weighted graph antar gedung kampus
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

def prim(graph, start):
    visited = set([start]) # gedung yang sudah terhubung ke jaringan
    edges = [] # kandidat kabel yang bisa dipasang (min-heap)

    # Masukkan semua pilihan kabel dari gedung awal
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor))

    mst = [] # daftar kabel yang dipilih untuk dipasang
    total_weight = 0  # total biaya pemasangan kabel

    while edges:
        weight, u, v = heapq.heappop(edges) # pilih kabel termurah

        if v not in visited: # pasang hanya jika gedung belum terhubung
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight 

            # Tambahkan pilihan kabel dari gedung yang baru terhubun
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# Jalankan Prim mulai dari GedungA
mst, total = prim(graph, 'GedungA')

print("Jaringan Kabel Minimum Antar Gedung:")
print("=" * 40)
for edge in mst:
    print(f"  {edge[0]} --> {edge[1]}, biaya = {edge[2]}")

print("=" * 40)
print(f"Total biaya minimum = {total}")

# ==========================================================
# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    Algoritma Prim. Dipilih karena graph ini termasuk dense
#    (setiap gedung terhubung ke hampir semua gedung lain),
#    dan Prim lebih efisien untuk kasus seperti ini dibanding
#    Kruskal yang harus mengurutkan semua edge terlebih dahulu.
#
# 2. Edge mana saja yang dipilih?
#    GedungA --> GedungC, biaya = 2
#    GedungC --> GedungD, biaya = 1
#    GedungD --> GedungB, biaya = 3
#
# 3. Berapa total biaya minimum?
#    Total biaya = 2 + 1 + 3 = 6
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    MST memastikan semua gedung terhubung ke jaringan internet
#    tanpa kabel berlebih (tidak ada cycle), sehingga
#    biaya pemasangan kabel menjadi seminimal mungkin.
# ==========================================================