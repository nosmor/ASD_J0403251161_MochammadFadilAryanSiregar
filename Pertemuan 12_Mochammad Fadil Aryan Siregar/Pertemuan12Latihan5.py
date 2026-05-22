# ==========================================================
# Nama  : Mochammad Fadil Aryan Siregar
# NIM   : J0403251161
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Representasi weighted graph antar kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bandung': 7},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Bandung': {}
}

# Fungsi Dijkstra untuk mencari jarak terpendek
def dijkstra(graph, start):

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak lebih besar dari data sebelumnya,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Memeriksa semua tetangga node
        for neighbor, weight in graph[current_node].items():

            # Menghitung jarak baru
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:

                # Update jarak
                distances[neighbor] = distance

                # Masukkan ke priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Menentukan node awal
start_node = 'Bogor'

# Menjalankan algoritma Dijkstra
hasil = dijkstra(graph, start_node)

# Menampilkan hasil jarak terpendek
print("Jarak terpendek dari Bogor:")

for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Node awal yang digunakan apa?
#    Bogor

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Depok (dengan jarak 2 dari Bogor).

# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Bandung (dengan total jarak terpendek 8, melalui rute Bogor -> Depok -> Jakarta -> Bandung)

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
#    Dijkstra mulai dari Bogor (0). Lalu mengecek tetangga terdekatnya yaitu Depok (2) dan Jakarta (5). 
#    Dari Depok, rute ke Jakarta diperbarui menjadi lebih kecil (2 + 2 = 4). Terakhir, dari Jakarta rute 
#    ke Bandung dihitung (4 + 7 = 11), namun rute optimal ke Bandung didapat dari akumulasi terkecil total jarak 8