'''
Write a program to Calculate Size of a tree
1.4
Size of a tree is the number of elements present in the tree. Size of the below tree is 5.

Example Tree
Example Tree

Size() function recursively calculates the size of a tree. It works as follows:

Size of a tree = Size of left subtree + 1 + Size of right subtree.
'''

import CdataS.BT.BianrySearchTree as tree

def treesize(root):
    if root == None:
        return 0
    return (treesize(root.left_child) + treesize(root.right_child) +1)


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
treesize(bst.root)
