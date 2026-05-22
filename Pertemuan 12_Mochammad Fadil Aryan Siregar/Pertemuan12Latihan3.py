# ==========================================================
# Nama  : Mochammad Fadil Aryan Siregar
# NIM   : J0403251161
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):

        for node in graph:
            for neighbor, weight in graph[node].items():

                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa bobot langsung dari A ke B?
#    5

# 2. Berapa total bobot jalur A -> C -> B?
#    2

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jalur A -> C -> B dengan total bobot 2 (lebih kecil dibanding rute langsung A -> B yang berbobot 5)

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Karena Bellman-Ford melakukan pemeriksaan ulang (relaksasi) ke semua edge berulang kali sebanyak (V-1) kali,
#    sehingga perubahan bobot akibat nilai negatif akan tetap terhitung dengan akurat

# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Proses memperbarui jarak terpendek ke suatu node jika ditemukan jalur baru melalui node tetangga yang total bobotnya lebih kecil
#

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    Dijkstra lebih cepat tapi gagal pada bobot negatif karena menggunakan prinsip greedy. Bellman-Ford lebih lambat karena 
#    memeriksa semua edge berulang kali, tetapi aman untuk bobot negatif