'''
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.

Idea:
1. If the node has a right sub-tree, then the next node will be the left most of the right sub-tree;
2. Otherwise, find the parent of the node until the node is the left child of its parent

Pseudocode
'''

import CdataS.tree

def inordersuccsor(tree, node):
    if node.right_child != None:
        newnode = node.right_child
        while (newnode.left_child != None):
            newnode = newnode.left_child
        return newnode
    else:
        newnode = node
        while(newnode.parent.value < newnode.value):
            newnode = newnode.parent
        return newnode

