'''
Find distance from root to given node in a binary tree
2.4
Given root of a binary tree and a key x in it, find distance of the given key from root. Distance means num­ber of
edges between two nodes.

Examples:

Input : x = 45,
        Root of below tree
        5
      /    \
    10      15
    / \    /  \
  20  25  30   35
       \
       45
Output : Distance = 3
There are three edges on path
from root to 45.

For more understanding of question,
in above tree distance of 35 is two
and distance of 10 is 1.
'''

import CdataS.BT.BianrySearchTree as tree
def nodedis(root, k):
    if root == None:
        return -1
    dis = -1
    if root.value == k or (nodedis(root.left_child, k) >=0) or(
            nodedis(root.right_child, k) >= 0):
        dis = max(dis,nodedis(root.left_child, k),nodedis(root.right_child, k))+1
    return dis






bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
l = [-1]
nodedis(bst.root, 8)



