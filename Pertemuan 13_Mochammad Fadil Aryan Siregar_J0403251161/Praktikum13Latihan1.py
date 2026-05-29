# =========================================
# Nama : Mochammad Fadil Aryan Siregar
# NIM : J0403251161
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# =========================================

edges = [
    ('A', 'B'), 
    ('A', 'C'), 
    ('A', 'D'), 
    ('C', 'D'), 
    ('B', 'D')  
]

spanning_tree = [
    ('A', 'C'), 
    ('C', 'D'),  
    ('D', 'B')  
]

print("Edge pada graph:")
for edge in edges:
    print(" ", edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(" ", edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki 5 edge dan mengandung cycle.
#    Spanning tree hanya memiliki 3 edge, menghubungkan semua
#    node tanpa cycle.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Cycle berarti ada jalur lebih antar node, sehingga ada edge
#    yang tidak diperlukan dan hanya menambah biaya tanpa manfaat.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Untuk menghubungkan node tanpa cycle, cukup n-1 edge.
#    Edge lebih dari itu pasti membentuk cycle.
# ==========================================================