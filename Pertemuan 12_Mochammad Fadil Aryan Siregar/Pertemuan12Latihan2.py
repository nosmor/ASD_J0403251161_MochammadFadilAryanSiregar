# ==========================================================
# Nama  : Mochammad Fadil Aryan Siregar
# NIM   : J0403251161
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
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

hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa jarak terpendek dari A ke B?
#    4

# 2. Berapa jarak terpendek dari A ke C?
#    2

# 3. Berapa jarak terpendek dari A ke D?
#    3

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    Karena total bobot rute A -> C -> D lebih kecil (2 + 1 = 3) 
#    dibandingkan rute A -> B -> D (4 + 5 = 9).

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Untuk memilih dan memproses node dengan jarak terkecil terlebih 
#    dahulu agar pencarian rute lebih efisien


# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Karena Dijkstra menganggap rute yang sudah dipilih sudah final. 
#    Bobot negatif bisa membuat rute yang sudah dilewati menjadi lebih 
#    pendek, sehingga hasilnya tidak akurat