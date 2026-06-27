# =========================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM : J0403251161
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# =========================================

import heapq

# Representasi graph sebagai adjacency dictionary
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},  # node A terhubung ke B(4), C(2), D(5)
    'B': {'A': 4, 'D': 3},           # node B terhubung ke A(4), D(3)
    'C': {'A': 2, 'D': 1},           # node C terhubung ke A(2), D(1)
    'D': {'A': 5, 'B': 3, 'C': 1}   # node D terhubung ke A(5), B(3), C(1)
}

def prim(graph, start):
    visited = set([start])   # set node yang sudah dikunjungi, dimulai dari node awal
    edges = []               # priority queue (min-heap) berisi kandidat edge

    # Masukkan semua edge dari node awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))  # format: (bobot, dari, ke)

    mst = []           # list untuk menyimpan edge MST
    total_weight = 0   # total bobot MST

    # Terus ambil edge terkecil selama masih ada kandidat
    while edges:
        weight, u, v = heapq.heappop(edges)  # ambil edge dengan bobot terkecil

        if v not in visited:                  # proses hanya jika node tujuan belum dikunjungi
            visited.add(v)                    # tandai node sebagai sudah dikunjungi
            mst.append((u, v, weight))        # tambahkan edge ke MST
            total_weight += weight            # akumulasi bobot

            # Tambahkan semua edge dari node baru ke heap (jika tetangganya belum dikunjungi)
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# Jalankan Prim mulai dari node 'A'
mst, total = prim(graph, 'A')

# Tampilkan hasil MST
print("Minimum Spanning Tree (Prim):")
for edge in mst:
    print(f"  {edge[0]} - {edge[1]}, bobot = {edge[2]}")

print("Total bobot =", total)
