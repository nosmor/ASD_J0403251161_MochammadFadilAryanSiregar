#Tugas Linked List Algoritma dan struktur data
#Mochammad Fadil Aryan Siregar TPL A1

#---------
#Latihan 5
#---------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):    
        self.head = None
        self.tail = None # Tambahkan pointer tail
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node # Tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node # Sambungkan tail ke node baru
            self.tail = new_node # Update tail ke node baru

    def reverse(self):
        prev = None
        current = self.head
                
        self.tail = self.head    
        while current is not None:
            next_node = current.next 
            current.next = prev      
            prev = current           
            current = next_node
        self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

ll = LinkedList()
print("Tampilan 1")
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)
print("Sebelum reverse:")
ll.display()
ll.reverse()
print("Setelah reverse:")
ll.display()

# print("Tampilan 2")
# ll.insert_at_end(10)
# ll.insert_at_end(20)
# ll.insert_at_end(30)
# ll.insert_at_end(40)
# print("Sebelum reverse:")
# ll.display()
# ll.reverse()
# print("Setelah reverse:")
# ll.display()

# print("Tampilan 3")
# ll.insert_at_end(7)
# print("Sebelum reverse:")
# ll.display()
# ll.reverse()
# print("Setelah reverse:")
# ll.display()