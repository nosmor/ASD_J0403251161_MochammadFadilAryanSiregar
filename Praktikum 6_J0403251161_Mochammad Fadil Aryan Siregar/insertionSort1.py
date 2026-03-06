# --------------------------------------
# Nama : Mochammad Fadil Aryan Siregar
# Kelas : TPL A1
# NIM : J0403251161
# --------------------------------------

def insertionSort(data):
    for i in range(1, len(data)):
        currentvalue = data[i]
        position = i
        while position>0 and data[position-1]>currentvalue :
            data[position] = data[position-1]
            position = position-1
            data[position] = currentvalue

data = [54,26,93,17,67,31,44,55,20]
insertionSort(data)
print(data)
