# ==========================================================
# Nama  : Mochammad Fadil Aryan Siregar
# NIM   : J0403251161
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")

for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Kantin (dengan waktu tempuh 2 menit)

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    9 menit (melalui rute Gerbang -> Kantin -> Aula yang total bobotnya 2 + 7 = 9)

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Tidak selalu. Jalur langsung bisa memiliki bobot besar, sedangkan rute memutar lewat node 
#    lain bisa memiliki akumulasi bobot yang lebih kecil


# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Karena semua bobot jalur (waktu tempuh) bernilai positif, sehingga algoritma Dijkstra 
#    dijamin akurat dan sangat efisien dalam mencari rute terpendek