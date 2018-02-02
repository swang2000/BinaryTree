'''
Find Minimum Depth of a Binary Tree
2.2
Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from root node down to the nearest leaf node.

For example, minimum height of below Binary Tree is 2.
Example Tree

Note that the path must end on a leaf node. For example, minimum height of below Binary Tree is also 2.
'''

import CdataS.BT.BianrySearchTree as tree
def treemindepth(root):
    if root == None:
        return 0
    if root.left_child == None and (root.right_child):
        return treemindepth(root.right_child) + 1
    elif root.right_child == None and (root.left_child):
        return treemindepth(root.right_child) + 1
    else:
        return min(treemindepth(root.left_child), treemindepth(root.right_child)) +1


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
treemindepth(bst.root)