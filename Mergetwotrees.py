'''
Merge Two Binary Trees by doing Node Sum (Recursive and Iterative)
2.5
Given two binary trees. We need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then
sum node values up as the new value of the merged node. Otherwise, the non-null node will be used as the node of new tree.

Example:

Input:
     Tree 1            Tree 2
       2                 3
      / \               / \
     1   4             6   1
    /                   \   \
   5                     2   7

Output: Merged tree:
         5
        / \
       7   5
      / \   \
     5   2   7
Note: The merging process must start from the root nodes of both trees.
'''

import CdataS.BT.BianrySearchTree as tree

def mergetree(root1, root2):
    if root1 == None and root2 == None:
        return
    if root1 and root2 == None:
        out = tree.Node(root1.value)
        out.left_child = mergetree(root1.left_child, None)
        out.right_child = mergetree(root1.right_child, None)
    if root2 and root1 == None:
        out = tree.Node(root2.value)
        out.left_child = mergetree(None, root2.left_child)
        out.right_child = mergetree(None, root2.right_child)
    if root1 and root2:
        out = tree.Node(root1.value + root2.value)
        out.left_child = mergetree(root1.left_child, root2.left_child)
        out.right_child = mergetree(root1.right_child, root2.right_child)
    return out



bst1 = tree.BST()
bst2 = tree.BST()
bst1.insert(4)
bst1.insert(2)
bst1.insert(1)
bst1.insert(5)

bst2.insert(3)
bst2.insert(1)
bst2.insert(2)
bst2.insert(6)
bst2.insert(7)
mergetree(bst1.root, bst2.root)



