class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class Linked_list:

    '''def appendleft(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            prev = self.head
            while prev.next:
                prev = prev.next
            prev.next = node
        self.length += 1'''
        
    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            node = self.head
            while node.next: #node.next is not None
                print(node.data, end = " → ")
                node = node.next
            print(node.data)

    def __str__(self):
        if self.head is None:
            return "Empty List"
        node = self.head
        string = ""
        while node.next:
            string += str(node.data) + " → "
            node = node.next
        return string + str(node.data)