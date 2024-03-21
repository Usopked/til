class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, node=None):
        self.root = node

    def preorder(node):
        def _preorder(node): 
            if node is None:
                return
            res.append(node.data)
            _preorder(node.left)
            _preorder(node.right)

        res = []
        _preorder(node)
        return res

    def inorder(self):
        def _inorder(node):
            if node is None:
                return
            _inorder(node.left)
            res.append(node.data)
            _inorder(node.right)

        res = []
        _inorder(self.root)
        return res

    def postorder(self):
        def _postorder(node):
            if node is None:
                return
            _postorder(node.left)
            _postorder(node.right)
            res.append(node.data)

        res = []
        _postorder(self.root)
        return res
    
    def levelorder(self):
        res = []
        if not self.root:
            return res
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            res.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
    
    def make_tree(self, arr):
        if not arr:
            return
        self.root = Node(arr[0])
        q = [self.root]
        index = 1
        while q and index < len(arr):
            node = q.pop(0)
            if index < len(arr) and arr[index] is not None:
                node.left = Node(arr[index])
                q.append(node.left)
            index += 1
            if index < len(arr) and arr[index] is not None:
                node.right = Node(arr[index])
                q.append(node.right)
            index += 1
    
if __name__ == "__main__":
    tree = Tree(Node("A"))
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    tree.root.left.left.left = Node("G")

    print("전위 순회 결과: ", tree.preorder())
    print("중위 순회 결과: ", tree.inorder())
    print("후위 순회 결과: ", tree.postorder())
    
    