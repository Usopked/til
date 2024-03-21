import sys
input = sys.stdin.readline
def find_pre(inorder, postorder):
    inorder_pos = {num: idx for idx, num in enumerate(inorder)}
    
    stack = [(0, len(inorder) - 1, 0, len(postorder) - 1)]
    pre_o = []

    while stack:
        in_left, in_right, post_left, post_right = stack.pop()
        if in_left > in_right or post_left > post_right:
            continue
        root = postorder[post_right]
        pre_o.append(root)
        inorder_root_index = inorder_pos[root]
        left_tree_size = inorder_root_index - in_left
        stack.append((inorder_root_index + 1, in_right, post_left + left_tree_size, post_right - 1))
        stack.append((in_left, inorder_root_index - 1, post_left, post_left + left_tree_size - 1))

    return pre_o


cnt = input()
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
print(*find_pre(inorder, postorder))
