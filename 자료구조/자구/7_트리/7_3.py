def preorder(tree):
    if not tree:
        return []
    res, stack = [], [0]

    while stack:
        index = stack.pop()
        res.append(tree[index])
        index = 2 * index + 2
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
        index -= 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
    return res


def inorder(tree):
    if not tree:
        return []
    index = 0
    res, stack = [], []

    while True:
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
            index = 2 * index + 1
        elif stack:
            index = stack.pop()
            res.append(tree[index])
            index = 2 * index + 2
        else:
            break
    return res

def postorder(tree):
    if not tree:
        return []
    res, stack = [], [0]
    visit_order = []

    while stack:
        index = stack.pop()
        visit_order.append(index)
        index = 2 * index + 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
        index = index + 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)

    while visit_order:
        index = visit_order.pop()
        res.append(tree[index])
    return res

