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
# preorder/ root-?left->right
# 12453
# postorder left->right->root
# 45231