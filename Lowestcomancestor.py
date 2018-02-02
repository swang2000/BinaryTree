'''
Lowest Common Ancestor in a Binary Search Tree.
2.3
Given values of two values n1 and n2 in a Binary Search Tree, find the Lowest Common Ancestor (LCA). You may assume that
 both the values exist in the tree.

BST_LCA
LCA of 10 and 14 is 12
LCA of 14 and 8 is 8
LCA of 10 and 22 is 20
Following is definition of LCA from Wikipedia:
Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 is defined as the lowest node in T that
has both n1 and n2 as descendants (where we allow a node to be a descendant of itself).

The LCA of n1 and n2 in T is the shared ancestor of n1 and n2 that is located farthest from the root. Computation of
lowest common ancestors may be useful, for instance, as part of a procedure for determining the distance between pairs
of nodes in a tree: the distance from n1 to n2 can be computed as the distance from the root to n1, plus the distance
from the root to n2, minus twice the distance from the root to their lowest common ancestor. (Source Wiki)
'''

import CdataS.BT.BianrySearchTree as tree
def LCA(root, n1, n2):
    while root != None:
        if root.value > n1 and root.value > n2:
            root = root.left_child
        elif root.value < n1 and root.value < n2:
            root = root.right_child
        else:
            break
    return root.value


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
LCA(bst.root, 2.5, 2)
