'''
Given a binary tree, return a list of level order traversal of the tree

'''
import CdataS.BT.BianrySearchTree as tree
def levelordertraversal(root):
    q = []
    b = []
    temp_node = root
    while temp_node != None:
        b.append(temp_node.value)
        if temp_node.left_child:
            q.append(temp_node.left_child)
        if temp_node.right_child:
            q.append(temp_node.right_child)
        if len(q) > 0:
            temp_node = q.pop(0)
        else:
            break
    return b

bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
levelordertraversal(bst.root)


