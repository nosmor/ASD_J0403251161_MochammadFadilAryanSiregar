# ==========================================================
# Nama  : Mochammad Fadil Aryan Siregar
# NIM   : J0403251161
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

jalur_1 = graph['A']['B'] + graph['B']['D']
jalur_2 = graph['A']['C'] + graph['C']['D']

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ==========================================================
# Jawaban :
# ==========================================================

# 1. Berapa total bobot jalur A -> B -> D?
#    9

# 2. Berapa total bobot jalur A -> C -> D?
#    3

# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jalur 2 (A -> C -> D) dengan total bobot 3

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge
#    Jumlah edge sedikit : bisa punya bobot besar (misal: jalan memutar atau macet).
#    Jumlah edge banyak : bisa punya total bobot kecil (misal: lewat jalan pintas)