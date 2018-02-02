'''
Print Right View of a Binary Tree
2.7
Given a Binary Tree, print Right view of it. Right view of a Binary Tree is set of nodes visible when tree is visited from Right side.

Right view of following tree is 1 3 7 8

          1
       /     \
     2        3
   /   \     /  \
  4     5   6    7
                  \
                   8
'''

import CdataS.BT.BianrySearchTree as tree
def treerightview(root, a=[]):
    if root == None:
        return
    a.append(root.value)
    if root.right_child:
        treerightview(root.right_child, a)
    elif root.left_child:
        treerightview(root.left_child, a)
    return a

bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(8)
bst.insert(6)
bst.insert(7)
a = treerightview(bst.root)

