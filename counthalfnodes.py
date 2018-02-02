'''
Count half nodes in a Binary tree (Iterative and Recursive)
2.4
Given A binary Tree, how do you count all the half nodes (which has only one child) without using recursion? Note leaves should not be touched as they have both children as NULL.

Input : Root of below tree

Output : 3
Nodes 7, 5 and 9 are half nodes as one of
their child is Null. So count of half nodes
in the above tree is 3
'''
import CdataS.BT.BianrySearchTree as tree
def counthalfnodes(root):
    q = []
    count = 0
    temp_node = root
    while temp_node:
        if (temp_node.left_child and (temp_node.right_child is None)) or (
            temp_node.left_child is None and temp_node.right_child):
            count += 1
        if temp_node.left_child:
            q.append(temp_node.left_child)
        if temp_node.right_child:
            q.append(temp_node.right_child)
        if len(q) > 0:
            temp_node = q.pop(0)
        else:
            break
    return count

bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
counthalfnodes(bst.root)
