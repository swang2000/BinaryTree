'''
Given preorder traversal of a binary search tree, construct the BST.

For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be root of following tree.

     10
   /   \
  5     40
 /  \      \
1    7      50

Solution:
1. Identify the root;
2. Code a list of index whose values are less than the root, and another list whose values are bigger than the root;
3. Split into two lists and recursively construct nodes

'''

import CdataS.BianrySearchTree as Tree

def constructBST(collection):
    if len(collection) == 0:
        return None
    node = Tree.Node(collection[0])
    left =  []
    right = []
    for i in range(1, len(collection)):
        if collection[i] < collection[0]:
            left.append(collection[i])
        else:
            right.append(collection[i])
    node.left_child = constructBST(left)
    node.right_child = constructBST(right)
    return node

L1 = constructBST([10, 5, 1, 7, 40, 50])
L1.preorder()
