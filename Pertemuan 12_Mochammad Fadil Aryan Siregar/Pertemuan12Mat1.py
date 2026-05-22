# ==========================================================
# Nama  : Mochammad Fadil Aryan Siregar
# NIM   : J0403251161
# Kelas : TPL A1
# ==========================================================

# ==========================================================
# Implementasi Algoritma Dijkstra
# ==========================================================

import heapq

# Representasi weighted graph menggunakan dictionary data structure
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Fungsi utama algoritma Dijkstra untuk mencari rute terpendek
def dijkstra(graph, start):
    # Menginisialisasi semua jarak node awal dengan nilai tak hingga (infinity)
    distances = {node: float('inf') for node in graph}
    # Jarak dari node awal ke dirinya sendiri diset bernilai 0
    distances[start] = 0
    
    # Inisialisasi priority queue (min-heap) dengan format data: (jarak, node)
    pq = [(0, start)]
    
    # Loop berjalan selama masih ada node yang harus diproses di dalam queue
    while pq:
        # Mengambil node dengan jarak kumulatif terkecil dari priority queue
        current_distance, current_node = heapq.heappop(pq)
        
        # Mengecek seluruh node tetangga beserta bobot edge dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Menghitung akumulasi jarak baru menuju node tetangga
            distance = current_distance + weight
            
            # Jika ditemukan jalur baru yang lebih pendek dari data sebelumnya
            if distance < distances[neighbor]:
                # Memperbarui nilai jarak terpendek di dictionary distances
                distances[neighbor] = distance
                # Memasukkan rute baru yang lebih efisien tersebut ke priority queue
                heapq.heappush(pq, (distance, neighbor))
                
    # Mengembalikan dictionary berisi hasil akhir jarak terpendek ke semua node
    return distances

# Menjalankan algoritma Dijkstra dengan titik mulai dari node 'A'
hasil = dijkstra(graph, 'A')

# Mencetak hasil kalkulasi jarak terpendek ke layar
print(hasil)

# ==========================================================
# Penjelasan Hasil
# ==========================================================
# A -> A = 0
# Karena node awal ke dirinya sendiri tidak memiliki biaya

# A -> B = 4
# Jalur langsung dari A ke B memiliki bobot 4

# A -> C = 2
# Jalur langsung dari A ke C memiliki bobot 2

# A -> D = 3
# Jalur terpendek diperoleh dari:
# A -> C -> D
# Total bobot = 2 + 1 = 3

# Jika melalui B:
# A -> B -> D = 4 + 5 = 9
# sehingga jalur tersebut tidak dipilih