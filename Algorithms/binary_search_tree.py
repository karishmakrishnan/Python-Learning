# binary search tree

    #     8
    #    / \
    #   3   10
    #  / \    \
    # 1   6    14
    #    / \
    #   4   7

# creating the node
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    if val > root.val:
        root.right = insert(root.right, val)
    return root
def inorder(root):
    if not root:
        return 
    inorder(root.left)
    print(root.val, end= " ")
    inorder(root.right)
def preorder(root):
    if not root:
        return
    print(root.val, end= " ")
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if not root:
        return
    postorder(root.left)
    preorder(root.right)
    print(root.val, end= " ")
values = [8, 3, 10, 1, 6, 14, 4, 7]
root = None
for val in values:
    root  = insert(root, val)

inorder(root)
