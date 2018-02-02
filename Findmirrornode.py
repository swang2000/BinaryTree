'''
Find mirror of a given node in Binary tree
3.7
Given a Binary tree, the problem is to find mirror of a given node. The mirror of a node is a node which exist at the
mirror position of node in opposite subtree at the root.

Examples:
mirror_nodes
mirror nodes

In above tree-
Node 2 and 3 are mirror nodes
Node 4 and 6 are mirror nodes.
'''

import CdataS.BT.BianrySearchTree as tree
def mirrornode(r1, r2, k):
    if r1 == None and r2 == None:
        return

    elif r1 and r2:
        if r1.value == k:
            return r2.value
        if r2.value == k:
            return r1.value
        else:
            t1 = mirrornode(r1.left_child, r2.right_child, k)
            t2 = mirrornode(r1.right_child, r2.left_child, k)
            if t1:
                return t1
            if t2:
                return t2
            else:
                return False

def findmirror(root, k):
    if root == None:
        return False
    if root.left_child and root.right_child:
        return mirrornode(root.left_child, root.right_child, k)


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
findmirror(bst.root, 4)
