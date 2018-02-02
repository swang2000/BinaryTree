'''
Print nodes between two given level numbers of a binary tree
2.6
Given a binary tree and two level numbers ‘low’ and ‘high’, print nodes from level low to level high.

For example consider the binary tree given in below diagram.

Input: Root of below tree, low = 2, high = 4

Output:
8 22
4 12
10 14
BST_LCA
'''
import CdataS.BT.BianrySearchTree as tree
def findnodebetween(root, n, m, l =0, a=[]):
    if root == None:
        return
    l = l +1
    if l >=n and l <=m:
        a.append(root.value)
    if root.left_child:
        findnodebetween(root.left_child, n, m, l, a)
    if root.right_child:
        findnodebetween(root.right_child, n, m, l, a)
    return a



bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
findnodebetween(bst.root, 2, 4)

