# --------------------------------------
# Nama : Mochammad Fadil Aryan Siregar
# Kelas : TPL A1
# NIM : J0403251161
# --------------------------------------

def bubbleSort(data):
    for num in range(len(data)-1,0,-1):
        for i in range(num):
            # agar descending, elemen data akan dibandingkan dan diubah ketika data[i] < data[i+1]
            if data[i]<data[i+1]:
            # untuk membandingkan dengan elemen yang bersebelahan kemudian ditukar jika memenuhi kondisi
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

data = [87,26,100,17,233,100,67,55,12,10000]
bubbleSort(data)
print(data)