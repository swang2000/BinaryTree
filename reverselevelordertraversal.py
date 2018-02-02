'''
Reverse Level Order Traversal
2.4
We have discussed level order traversal of a post in previous post. The idea is to print last level first, then second
last level, and so on. Like Level order traversal, every level is printed from left to right.

Example Tree
Example Tree

Reverse Level order traversal of the above tree is “4 5 2 3 1”.

Both methods for normal level order traversal can be easily modified to do reverse level order traversal.
'''
import CdataS.BT.BianrySearchTree as tree
def rlot(root):
    q = []
    t = []
    s = []
    temp_node = root
    while temp_node:
        s.append(temp_node.value)
        if temp_node.right_child:
            q.append(temp_node.right_child)
        if temp_node.left_child:
            q.append(temp_node.left_child)
        if len(q) >0:
            temp_node = q.pop(0)
        else:
            break
    while len(s) >0:
        t.append(s.pop())
    return t

bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
rlot(bst.root)

