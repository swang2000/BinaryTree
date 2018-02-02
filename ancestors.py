'''
Print Ancestors of a given node in Binary Tree
2.5
Given a Binary Tree and a key, write a function that prints all the ancestors of the key in the given binary tree.

For example, if the given tree is following Binary Tree and key is 7, then your function should print 4, 2 and 1.


              1
            /   \
          2      3
        /  \
      4     5
     /
    7
'''

import CdataS.BT.BianrySearchTree as tree
def ancestors(root, k):
    if root == None:
        return False
    if root.value == k:
        return True
    else:
        if ancestors(root.left_child, k) or ancestors(root.right_child, k):
            print(root.value)
            return True





bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
ancestors(bst.root, 2.5)

