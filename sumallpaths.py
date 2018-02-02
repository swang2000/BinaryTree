'''
Sum of all the numbers that are formed from root to leaf paths
2.5
Given a binary tree, where every node value is a Digit from 1-9 .Find the sum of all the numbers which are formed from root to leaf paths.

For example consider the following Binary Tree.

                                          6
                                      /      \
                                    3          5
                                  /   \          \
                                 2     5          4
                                      /   \
                                     7     4
  There are 4 leaves, hence 4 root to leaf paths:
   Path                    Number
  6->3->2                   632
  6->3->5->7               6357
  6->3->5->4               6354
  6->5>4                    654
Answer = 632 + 6357 + 6354 + 654 = 13997
'''

import CdataS.BT.BianrySearchTree as tree
def sumallpaths(root, val=0):
    if root == None:
        return 0
    val = 10 * val + root.value
    if root.left_child == None and (root.right_child == None):
        return val
    return (sumallpaths(root.left_child, val) + sumallpaths(root.right_child, val))

bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(8)
bst.insert(6)
bst.insert(7)
sumallpaths(bst.root)