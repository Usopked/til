class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def __contains__(self, data):
        node = self.root
        while node:
            if node.data == data:
                return True
            elif node.data > data:
                node = node.left
            else:
                node = node.right
        return False

    def inorder(self):
        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            res.append(node.data)
            _inorder(node.right)
        res = []
        _inorder(self.root)
        return res

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if node.data > data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node

    def insert(self, data):        
        self.root = self._insert(self.root, data)