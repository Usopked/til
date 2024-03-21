class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node to the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the linked list is empty
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Add a new node to the beginning of the linked list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Print the linked list
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Testing the generalized code with the Node class included
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.prepend(0)
llist.append(4)

llist.print_list()  # Expected output: 0 -> 1 -> 2 -> 3 -> 4 -> None


















'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

node = head
while node:
    if node.next is None:
        node.next = Node(4)
        break
    node = node.next

node = Node(0)
node.next = head
head = node
'''