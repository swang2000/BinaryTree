'''
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL).
The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL.
The order of nodes in DLL must be same as Inorder of the given Binary Tree.
The first node of Inorder traversal (left most node in BT) must be head node of the DLL.
'''


import CdataS.BT.BianrySearchTree as tree

def fixprevptr(root, prevptr):
    if root is not None:
        fixprevptr(root.left_child, prevptr)
        root.left_child = prevptr[0]
        prevptr[0] = root
        fixprevptr(root.right_child, prevptr)




def fixnextptr(root,prev=None ):
    while root and root.right_child != None:
        root = root.right_child

    while root and root.left_child is not None:
        prev = root
        root = root.left_child
        root.right_child = prev

    return root

def printDLL(a):
    while a != None:
        print(a.value)
        a = a.right_child


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
prev =[None]
fixprevptr(bst.root, prev)
dll = fixnextptr(bst.root)
printDLL(dll)