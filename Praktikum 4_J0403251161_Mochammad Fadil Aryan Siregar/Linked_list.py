#-------------------------------------
# Nama : Mochammad Fadil Aryan Siregar
# NIM : J0403251161
# Kelas : TPL A1
#-------------------------------------

# ===============================================
#Implementasi Dasar : Node pada Linked List
# ===============================================

class Node:
    #instant Constructor (izin pake bahasa inggris bu)
    def __init__(self,data):
        self.data = data 
        self.next = None

#1) Membuat Node dgn intantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Connecting each Node A -> B -> C -> None
head = nodeA
tail = nodeC
nodeA.next = nodeB
nodeB.next = nodeC

#3) Node Traversal, from Head to None
current = head
while current is not None :
    print(current.data) #To show the current Data
    current = current.next #to the next Node
