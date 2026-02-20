#-------------------------------------
# Nama : Mochammad Fadil Aryan Siregar
# NIM : J0403251161
# Kelas : TPL A1
#-------------------------------------

# ===============================================
#Implementasi Dasar : Queue
# ===============================================

class Node:
    #instant Constructor (izin pake bahasa inggris bu)
    def __init__(self,data):
        self.data = data 
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self,data): #Insert Data
        node_baru = Node(data)

        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = node_baru
            self.rear = node_baru
            return
        #Jika queue tidak kosong maka akan lgsg letakkan data baru setelah rear dan menjadikannya rear baru
        self.rear.next = node_baru #Place new data after the rear (tail)
        self.rear = node_baru #Replace rear with the new data

    def dequeue(self): #Delete Data
        data_terhapus = self.front.data #Lihat data paling depan
        self.front = self.front.next #geser front ke Node baru

        #Kalau mendorong front menjadi None
        if self.is_empty():
            self.rear = None
            print("Queue is empty")
        return data_terhapus

    def tampilan(self):
        current = self.front
        print("Front", end="-->")
        while current is not None:
            print(current.data, end="-->")
            current = current.next
        print("Rear")

q = queue()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.tampilan()
q.dequeue()
q.tampilan()
q.dequeue()
q.tampilan()
q.dequeue()
q.tampilan()


