'''

Given a Binary Tree, convert it to a Binary Search Tree. The conversion must be done in such a way that keeps the original structure of Binary Tree.
Example 1
Input:
          10
         /  \
        2    7
       / \
      8   4
Output:
          8
         /  \
        4    10
       / \
      2   7


Example 2
Input:
          10
         /  \
        30   15
       /      \
      20       5
Output:
          15
         /  \
       10    20
       /      \
      5        30

solution:
1. Do an in-order traversal to create a list to hold all elements of binary tree;
2. Sort the list;
3. Do an in-order traversal for the old tree and copy the new values from the sorted list into the tree


'''

import CdataS.BianrySearchTree as BST

def btTolist(root, alist =[]):
    if root == None:
        return
    btTolist(root.left_child, alist)
    alist.append(root.value)
    btTolist(root.right_child, alist)

def listToBST(alist, bst):
    if bst == None:
        return
    listToBST(alist, bst.left_child)
    bst.value = alist.pop(0)
    listToBST(alist, bst.right_child)


