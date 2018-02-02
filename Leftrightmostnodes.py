'''
Print leftmost and rightmost nodes of a Binary Tree
2.5
Given a Binary Tree, Print the corner nodes at each level. The node at the leftmost and the node at the rightmost.

For example, output for following is 15, 10, 20, 8, 25.
'''
import CdataS.BT.BianrySearchTree as tree
def LRM(root):
    if root == None:
        return
    out = [root.value]
    temp = root
    while temp.left_child:
        out.append(temp.left_child.value)
        temp = temp.left_child
    temp = root
    while temp.right_child:
        out.append(temp.right_child.value)
        temp = temp.right_child
    return out



bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
LRM(bst.root)


bst2 = tree.BST()
bst2.insert(15)
bst2.insert(10)
bst2.insert(8)
bst2.insert(12)
bst2.insert(20)
bst2.insert(16)
bst2.insert(25)
LRM(bst2.root)