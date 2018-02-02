'''
Print all nodes that don’t have sibling
2.1
Given a Binary Tree, print all nodes that don’t have a sibling (a sibling is a node that has same parent. In a Binary
Tree, there can be at most one sibling). Root should not be printed as root cannot have a sibling.

For example, the output should be “4 5 6” for the following tree.

Binary Tree

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.

This is a typical tree traversal question. We start from root and check if the node has one child, if yes then print
the only child of that node. If node has both children, then recur for both the children.
'''

import CdataS.BT.BianrySearchTree as tree

def onesibling(root):
    if root == None:
        return
    if root.left_child and root.right_child is None:
        print (root.left_child.value)
        onesibling(root.left_child)
    elif  root.right_child and root.left_child is None:
        print (root.right_child.value)
        onesibling(root.right_child)
    else:
        onesibling(root.left_child)
        onesibling(root.right_child)
        return



bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
onesibling(bst.root)

