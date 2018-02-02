'''
Root to leaf path sum equal to a given number
2.4
Given a binary tree and a number, return true if the tree has a root-to-leaf path such that adding up all the values
along the path equals the given number. Return false if no such path can be found.



For example, in the above tree root to leaf paths exist with following sums.

21 –> 10 – 8 – 3
23 –> 10 – 8 – 5
14 –> 10 – 2 – 2

So the returned value should be true only for numbers 21, 23 and 14. For any other number, returned value should be false.
'''

import CdataS.BT.BianrySearchTree as tree

def checksumtoleaf(root, sum):
    if root == None:
        return False

    if root.value == sum:
        return True
    else:
        if checksumtoleaf(root.left_child, sum - root.value) or checksumtoleaf(root.right_child, sum - root.value):
            return True
        else:
            return False




bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
checksumtoleaf(bst.root, 20)
