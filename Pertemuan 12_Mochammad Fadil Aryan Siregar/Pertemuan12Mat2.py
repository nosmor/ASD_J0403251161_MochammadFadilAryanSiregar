# ==============================================================================
# Nama  : Mochammad Fadil Aryan Siregar
# NIM   : J0403251161
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path
# ==============================================================================

# ==============================================================================
# Implementasi Algoritma Bellman-Ford
# ==============================================================================

def bellman_ford(graph, start):
    # Menginisialisasi semua jarak node awal dengan nilai tak hingga (infinity)
    distances = {node: float('inf') for node in graph}
    # Jarak dari node awal ke dirinya sendiri diset bernilai 0
    distances[start] = 0
    
    # ==========================================================================
    # Proses Relaksasi Edge
    # ==========================================================================
    # Loop utama berjalan sebanyak (jumlah node - 1) kali
    for _ in range(len(graph) - 1):
        
        # Memeriksa setiap node yang ada di dalam graph
        for node in graph:
            
            # Memeriksa semua node tetangga dan bobot edge dari node saat ini
            for neighbor, weight in graph[node].items():
                # Jika rute baru melalui node ini menghasilkan total bobot lebih kecil
                if distances[node] + weight < distances[neighbor]:
                    # Memperbarui nilai jarak terpendek menuju node tetangga tersebut
                    distances[neighbor] = distances[node] + weight
                    
    # Mengembalikan dictionary berisi hasil akhir jarak terpendek dari start node
    return distances

# # ==============================================================================
# Penjelasan Algoritma
# ==============================================================================
# Bellman-Ford bekerja dengan cara:
# 1. Mengatur jarak awal semua node menjadi tak hingga (inf) dan node mulai menjadi 0.
# 2. Melakukan perulangan (relaksasi) untuk semua edge sebanyak (jumlah node - 1) kali.
# 3. Memperbarui jarak ke node tetangga jika ditemukan rute yang total bobotnya lebih kecil.
# 4. Melalui pengulangan ini, algoritma bisa menghitung bobot negatif dengan akurat.