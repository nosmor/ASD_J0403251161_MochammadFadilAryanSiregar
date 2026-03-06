# --------------------------------------
# Nama : Mochammad Fadil Aryan Siregar
# Kelas : TPL A1
# NIM : J0403251161
# --------------------------------------

def selectionSort(data):
    for fillslot in range(len(data)-1,0,-1):
        positionOfMax=0
        for location in range(1, fillslot+1):
            if data[location] > data[positionOfMax]:
                positionOfMax = location
        #Tukar
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp
    
data = [34,55,60,92,76,12,44,67,29]
selectionSort(data)
print(data)