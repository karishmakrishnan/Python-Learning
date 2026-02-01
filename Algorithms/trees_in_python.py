# trees in python

# trees in python is a heirarchiel data structure with root and nodes
# Terminology
# Root: top node
# Parent / Child
# Leaf: node with no children
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
# simple node structure
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
# DFS (Depth first search)/ Inorder(left->root->right)
# 4 2 5 1 3
# preorder/ root->left->right
# 12453
# postorder left->right->root
# 45231

# inorder
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

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


inorder(root)
print("\n")
preorder(root)
print("\n")
postorder(root)