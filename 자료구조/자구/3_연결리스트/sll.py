#파일 이름: sllist.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None:
            return "Empty List"
        node = self.head
        string = ""
        while node.next:
            string += str(node.data) + " → "
            node = node.next
        return string + str(node.data)

    def __contains__(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

    def appendleft(self, data):
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
        self.length += 1

    def popleft(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node.data

    def pop(self):
        if self.head is None:
            return None
        node = self.head
        if self.head.next is None:
            self.head = None
        else:
            while node.next is not None:
                prev = node
                node = node.next
            prev.next = None
        self.length -= 1
        return node.data

    def insert(self, i, data):
        if i <= 0:
            self.appendleft(data)
        elif i >= self.length:
            self.append(data)
        else:
            prev = self.head
            for _ in range(i - 1):
                prev = prev.next
            node = Node(data)
            node.next = prev.next
            prev.next = node
            self.length += 1

    def remove(self, data):
        if self.head.data == data:
            self.popleft()
            return True
        prev = self.head
        while prev.next:
            if prev.next.data == data:
                prev.next = prev.next.next
                self.length -= 1
                return True
            prev = prev.next
        return False

    def reverse(self):
        if self.length <= 1:
            return
        ahead = self.head.next
        prev = self.head
        prev.next = None
        while ahead:
            self.head = ahead
            ahead = ahead.next
            self.head.next = prev
            prev = self.head


#위에서 만든 단일 연결 리스트를 불러와서 실행한다.
