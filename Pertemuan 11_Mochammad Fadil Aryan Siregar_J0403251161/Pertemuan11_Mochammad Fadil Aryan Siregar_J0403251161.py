# ==============================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM : J0403251161
# Kelas : TPL A1
# Algoritma dan struktur data Pertemuan 11
# ==============================================


# Praktikum 1 - membuat adjecency matrix
# ==============================================


print("\nPraktikum 1 Adjecency Matriks\n"
      "=============================")
    # 1 Adjacency Matrix
# Diketahui [(0, 1), (0, 2), (1, 2), (2, 3)]
def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    for it in edges:
        # 2 baris dibawah merepresentasikan index pada sub-list yang dikasih, misal (0,1) maka (u, v)
        u = it[0]
        v = it[1]

        mat[u][v] = 1 # Menunjukkan ada jalan dari u ke v
        mat[v][u] = 1
    return mat

if __name__ =="__main__":
    V = 4

    # Vertex yang terhubung edges
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)] # edges ini menunjukkan data-data yang terhubung dengan dengan sebelahnya
    # Bisa dilihat pada data diatas, angka 0 terhubung dengan 1 dan 2
    # 1 terhubung dengan 0 dan 2
    # yang terakhir 2 terhubung dengan 0, 1, dan 3

    # Memanggil fungsi untuk membuat graph
    mat = createGraph(V, edges)

    # Tampilan matrix
    print("Tampilan Adjecency Matrix")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()

          
print("\nPraktikum 2 Adjecency list\n"
      "=============================")
    # 2 Adjacency List
# diketahui [(A,B),(A,C),(B,D),(D,C)]
def createGraphADJ(V, edges):
    adj = {i: [] for i in V}
    
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

if __name__ == "__main__":
    V2 = ['A', 'B', 'C', 'D']
    edges = [('A','B'), ('A','C'), ('B','D'), ('D','C')]
    
    adj = createGraphADJ(V2, edges)
    
    print("Tampilan Adjacency List")
    # Penampilan List yang menggunakan looping dictionary
    for i in V2:
        print(f"{i}: ", end="")
        for n in adj[i]:
            print(n, end=" ")
        print()


print("\nPraktikum 3 Mengkonversi matrix ke list\n"
      "=============================")
    # Praktikum 3 Konversi matriks ke list
# Diketahui matriks
matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

def convertToADJList(matr):
    adj_list = []

    # Looping setiap baris (i)
    for i in range(len(matr)):
        # List bawah ini digunakan untuk memasukkan angka yang terkoneksi pada vertex
        adjacent = []
        # Loop kolom J
        for j in range(len(matr[i])):
            # Jika isinya 1, maka j adalah tetangga dari i
            if matr[i][j] == 1:
                adjacent.append(j)
        # Masukkan daftar tetangga tadi ke list utama
        adj_list.append(adjacent)
        
    return adj_list

# Eksekusi
conv = convertToADJList(matrix)
# Tampilan
print("Adjacency List (Representasi Angka):")
for i in range(len(conv)):
    print(f"{i}: {conv[i]}")


print("\nPraktikum 4 Studi kasus\n"
      "=============================")
    # Praktikum 4 studi kasus 
# Fungsi untuk membangun Adjacency List
def createGraphADJUnd(V, edges):
    # Membuat list kosong sebanyak V
    adj = [[] for _ in range(V)]
    
    # Memasukkan setiap edge kedalam list
    for it in edges:
        u = it[0]
        v = it[1]
        
        adj[u].append(v)
        adj[v].append(u)
    return adj

def createGraphUnd(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    for it in edges:
        # 2 baris dibawah merepresentasikan index pada sub-list yang dikasih, misal (0,1) maka (u, v)
        u = it[0]
        v = it[1]

        mat[u][v] = 1 # Menunjukkan ada jalan dari u ke v
        mat[v][u] = 1
    return mat

if __name__ == "__main__":
    # Inisialisasi Data
    user_names = ["Leon", "Fadil", "Vergil", "Dante", "Evanescia"]
    V5 = len(user_names)
    
    # Daftar hubungan (edges)
    friend = [(0,1), (0,2), (1,3), (2,3), (3,4)]
    
    # Membangun matriks
    hasil = createGraphUnd(V5, friend)
    print("# Tampilan Adjecency Matrix")
    for i in range(V5):
        for j in range(V5):
            print(hasil[i][j], end=" ")
        print()


    adj = createGraphADJUnd(V5, friend)
    print("\n# Tampilan Adjacency List")
    # Penampilan List yang menggunakan looping dictionary
    for i in range(V5):
        print(f"{user_names[i]}: ", end="")
        for n in adj[i]:
            print(user_names[n], end=" ")
        print()
