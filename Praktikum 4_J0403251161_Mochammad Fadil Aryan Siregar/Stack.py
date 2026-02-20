#-------------------------------------
# Nama : Mochammad Fadil Aryan Siregar
# NIM : J0403251161
# Kelas : TPL A1
#-------------------------------------

# ===============================================
#Implementasi Dasar : Stack
# ===============================================

class Node:
    #instant Constructor (izin pake bahasa inggris bu)
    def __init__(self,data):
        self.data = data 
        self.next = None

#Push(Insert head) and Pop(Deletes head) in Stack
# Example, if A-> B -> C -> None, pop(head) therefore B -> C -> None

class stack:
    def __init__(self):
        self.top = None #menunjuk node paling atas (awalnya kosong)

    def push(self,data): #Insert Data
        #1 Crete Node
        nodebaru = Node(data) #instant constructor
        #2 pointing the top (old Node) from the new node
        nodebaru.next = self.top
        #3 switch old Node with the new one
        self.top = nodebaru

    def is_empty(self):
        return self.top is None

    def pop(self): #Delete Node
        if self.is_empty():
            print("stack is empty")
            return None
       
        data_terhapus = self.top.data #Sorot top dan simpan di variabel
        # B -> A -> None
        self.top = self.top.next
        return data_terhapus
    
    def peek(self): #To peek at the top
        if self.is_empty():
            print("stack is empty")
            return None
        return self.top.data

    def display(self):
        # Top -> A -> B
        current = self.top
        print("Top", end="-->")
        while current is not None:
            print(current.data, end="-->")
            current = current.next
        print("None")

x = stack()
x.push('A')
x.push('B')
x.push('C')
x.display()
print("Current top :", x.peek())
x.pop()
x.display()
x.pop()
x.display()
x.pop()
x.display()
print("Final top :", x.peek())