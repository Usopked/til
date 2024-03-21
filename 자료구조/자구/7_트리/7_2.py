def preorder(tree, i=0):
    if i < len(tree):
        print(tree[i], end = " ") #방문 처리(출력)
        left = 2 * i + 1
        right = left + 1    
        if left < len(tree) and tree[left] is not None:
            preorder(tree, left)
        if right < len(tree) and tree[right] is not None:
            preorder(tree, right)



tree = ["A", "B", "C", "D", "E", "F", None, "G"]

def preorder(tree):  
    def _preorder(tree, i = 0):
        if i >= len(tree) or tree[i] is None: #인덱스를 벗어나거나, 원소가 None이면 종료
            return
        res.append(tree[i])
        left = 2 * i + 1
        right = left + 1    
        _preorder(tree, left)
        _preorder(tree, right)

    res = []    
    _preorder(tree)
    return res

def inorder(tree):
    def _inorder(tree, i = 0):
        if i >= len(tree) or tree[i] is None:
            return
        left = 2 * i + 1
        right = left + 1
        _inorder(tree, left)
        res.append(tree[i])
        _inorder(tree, right)

    res = []    
    _inorder(tree)
    return res

def postorder(tree):
    def _postorder(tree, i = 0):
        if i >= len(tree) or tree[i] is None:
            return
        left = 2 * i + 1
        right = left + 1
        _postorder(tree, left)
        _postorder(tree, right)
        res.append(tree[i])

    res = []    
    _postorder(tree)
    return res


'''def preorder(tree):  
    def _preorder(tree, i = 0):
        if i < len(tree):
            res.append(tree[i])
            left = 2 * i + 1
            right = left + 1    
            if left < len(tree) and tree[left] is not None:
                _preorder(tree, left)
            if right < len(tree) and tree[right] is not None:
                _preorder(tree, right)          
    res = []    
    _preorder(tree)
    return res'''


'''res = []

def preorder(tree, i=0):
    global res
    if i < len(tree):
        res.append(tree[i])
        left = 2 * i + 1
        right = left + 1    
        if left < len(tree) and tree[left] is not None:
            preorder(tree, left)
        if right < len(tree) and tree[right] is not None:
            preorder(tree, right)

preorder(tree)
print(res)
'''

'''def preorder(tree, i=0):
    if i < len(tree):
        res = [tree[i]]
        left = 2 * i + 1
        right = left + 1    
        if left < len(tree) and tree[left] is not None:
            res += preorder(tree, left)
        if right < len(tree) and tree[right] is not None:
            res += preorder(tree, right)
        return res
'''