'''
Program to count leaf nodes in a binary tree
1.6
A node is a leaf node if both left and right child nodes of it are NULL.

Here is an algorithm to get the leaf node count.
'''

import CdataS.BT.BianrySearchTree as tree
def countleaf(root):
    # size = 0
    if root == None:
        size = 0
        return size
    else:
        if root.left_child == None and (root.right_child == None):
            size = 1
            return size
        else:
            return (countleaf(root.left_child) + countleaf(root.right_child))


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
countleaf(bst.root)