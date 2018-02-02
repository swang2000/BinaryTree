'''
Lowest Common Ancestor in a Binary Tree | Set 1
3.5
Given a binary tree (not a binary search tree) and two values say n1 and n2, write a program to find the least common ancestor.
'''

import CdataS.BT.BianrySearchTree as tree
def findLCA(a, n1, n2):
    if a == None:
        return

    if a.value == n1 or (a.value == n2):
        return a.value

    left_lca = findLCA(a.left_child, n1, n2)
    right_lca = findLCA(a.right_child, n1, n2)

    if left_lca and right_lca:
        return a.value

    return left_lca if left_lca else right_lca


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
findLCA(bst.root, 2.5, 4)
