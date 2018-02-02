'''
A program to check if a binary tree is BST or not
3
A binary search tree (BST) is a node based binary tree data structure which has the following properties.
• The left subtree of a node contains only nodes with keys less than the node’s key.
• The right subtree of a node contains only nodes with keys greater than the node’s key.
• Both the left and right subtrees must also be binary search trees.
'''

import CdataS.BT.BianrySearchTree as tree

INT_MIN = - 2**31
INT_MAX = 2**31

def checkBST(a, INT_MIN, INT_MAX):
    if a == None:
        return True
    if a.value < INT_MIN or a.value > INT_MAX:
        return False
    else:
        return checkBST(a.left_child, INT_MIN, a.value) and checkBST(a.right_child, a.value, INT_MAX)


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
checkBST(bst.root, INT_MIN, INT_MAX)
