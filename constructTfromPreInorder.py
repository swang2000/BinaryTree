'''
Construct Tree from given Inorder and Preorder traversals
Let us consider the below traversals:

Inorder sequence: D B E A F C
Preorder sequence: A B D E C F
'''

import CdataS.BT.BianrySearchTree as tree
def Tree_Pre_Inorder(a, b):
    if len(a) >0:
        root = tree.Node(a[0])
        index  = b.index(a[0])
        lefta = a[1:index+1]
        leftb = b[:index]
        righta = a[index+1:]
        rightb = b[index+1:]
        root.left_child = Tree_Pre_Inorder(lefta, leftb)
        root.right_child = Tree_Pre_Inorder(righta, rightb)
        return root


a = [1,2,4,5,6,3,8,7]
b=  [4,2,6,5,1,3,7,8]

c= Tree_Pre_Inorder(a, b)



