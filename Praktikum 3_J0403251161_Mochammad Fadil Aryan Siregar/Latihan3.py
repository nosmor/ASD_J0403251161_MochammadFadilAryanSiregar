#Tugas Linked List Algoritma dan struktur data
#Mochammad Fadil Aryan Siregar TPL A1

#---------
#Latihan 3
#---------

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class circularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head #Biar balik lagi
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def display_forward(self):
        if not self.head:
            print("List is empty")
            return
        print("\nTraversing forward:")
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break

        print("...(back to head)")

    def display_backward(self):
        if not self.head:
            print("List is empty")
            return
        print("\nTraversing backward:")
        tail = self.head.prev
        temp = tail
        print(temp.data, end=" -> ")
        temp = temp.prev

        while temp != self.head.prev:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("...(back to tail)")

    def search(self, key):
        if not self.head:
            print("List is empty")
            return False
        temp = self.head
        found = False

        while True:
            if temp.data == key:
                found = True
                break
            temp = temp.next
            if temp == self.head:
                break

        if found:
            print(f"Elemen {key} Found")
        else:
            print(f"Elemen {key} Not Found")
        return found

cdll = circularDoublyLinkedList()
cdll.insert_at_end(3)
cdll.insert_at_end(5)
cdll.insert_at_end(13)
cdll.insert_at_end(2)

cdll.display_forward()
cdll.display_backward()
cdll.search(5)
