'''
Write an Efficient Function to Convert a Binary Tree into its Mirror Tree
1.8
Mirror of a Tree: Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged.

MirrorTree1
Trees in the above figure are mirror of each other
'''

import CdataS.BT.BianrySearchTree as tree
def mirrortree(root):
    if root == None:
        return
    mroot = tree.Node(root.value)
    mroot.left_child = mirrortree(root.right_child)
    mroot.right_child = mirrortree(root.left_child)
    return mroot



bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
a = mirrortree(bst.root)
