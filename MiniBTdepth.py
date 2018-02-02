'''
Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from root node down to the nearest leaf node.
'''

import CdataS.BianrySearchTree as BST
def miniBTdepth(bt):
    if bt == None:
        return 0
    if bt.left_child == None and bt.right_child == None:
        return 1
    if bt.left_child and bt.right_child == None:
        return miniBTdepth(bt.left_child) + 1
    if bt.right_child and bt.left_child == None:
        return miniBTdepth(bt.right_child) + 1
    if bt.left_child and bt.right_child:
        return min(miniBTdepth(bt.left_child) + 1, miniBTdepth(bt.right_child) + 1)

bst = BST.BST()
bst.insert(8)
bst.insert(7)
bst.insert(9)
bst.insert(6)
bst.insert(5)
bst.insert(4)
depth = miniBTdepth(bst.root)


