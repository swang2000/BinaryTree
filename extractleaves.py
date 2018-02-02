'''
Extract Leaves of a Binary Tree in a Doubly Linked List
2.8
Given a Binary Tree, extract all leaves of it in a Doubly Linked List (DLL). Note that the DLL need to be created in-place.
Assume that the node structure of DLL and Binary Tree is same, only the meaning of left and right pointers are different.
In DLL, left means previous pointer and right means next pointer.

Let the following be input binary tree
        1
     /     \
    2       3
   / \       \
  4   5       6
 / \         / \
7   8       9   10


Output:
Doubly Linked List
7<->8<->5<->9<->10

Modified Tree:
        1
     /     \
    2       3
   /         \
  4           6
'''

import CdataS.BT.BianrySearchTree as tree


def extractleaves(root, a=[]):
    if root == None:
        return
    if root.left_child == None and root.right_child == None:
        a.append(root.value)
    if root.left_child:
        extractleaves(root.left_child, a)
    if root.right_child:
        extractleaves(root.right_child, a)
    return a

bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
extractleaves(bst.root)


def extractleavesDLL(root, pre = None):
    if root == None:
        return
    if root.left_child == None and (root.right_child) == None:
        root.left_child = pre
        if pre:
            pre.left_child = root
        pre = root
    if root.left_child:
        extractleavesDLL(root.left_child, pre)
    if root.right_child:
        extractleavesDLL(root.right_child, pre)
    return root

