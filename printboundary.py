'''
Boundary Traversal of binary tree
3.5
Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root. For example,
boundary traversal of the following tree is “20 8 4 10 14 25 22”


'''


import CdataS.BT.BianrySearchTree as tree

def printboundary(root):
    if root != None:
        print(root.value)
        printleft(root.left_child)
        printleaves(root.left_child)
        printleaves(root.right_child)
        printright(root.right_child)


def printleft(root):
    if root != None:
        if root.left_child:
            print (root.value)
            printleft(root.left_child)
        elif root.right_child:
            print(root.value)
            printleft(root.right_child)




def printleaves(root):
    if root != None:
        printleaves(root.left_child)
        if root.left_child == None and root.right_child == None:
            print(root.value)
        printleaves(root.right_child)


def printright(root):
    if root != None:
        if root.right_child:
            printright(root.right_child)
            print(root.value)
        elif root.left_child:
            printright(root.left_child)
            print(root.value)



bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
printboundary(bst.root)


