'''
Foldable Binary Trees
2.6
Question: Given a binary tree, find out if the tree can be folded or not.

A tree can be folded if left and right subtrees of the tree are structure wise mirror image of each other. An empty tree is considered as foldable.

Consider the below trees:
(a) and (b) can be folded.
(c) and (d) cannot be folded.

(a)
       10
     /    \
    7      15
     \    /
      9  11

(b)
        10
       /  \
      7    15
     /      \
    9       11

(c)
        10
       /  \
      7   15
     /    /
    5   11

(d)

         10
       /   \
      7     15
    /  \    /
   9   10  12
'''

import CdataS.BT.BianrySearchTree as tree
def checkfoldable(r1, r2):
    if r1 == None and (r2 ==  None):
        return True

    elif r1 == None or (r2 == None):
        return False

    return checkfoldable(r1.left_child, r2.right_child) and checkfoldable(r1.right_child, r2.left_child)


def isfoldable(root):
    if root == None:
        return True
    return checkfoldable(root.left_child, root.right_child)


bst = tree.BST()
bst.insert(10)
bst.insert(7)
bst.insert(6)
bst.insert(11)
bst.insert(15)
isfoldable(bst.root)




