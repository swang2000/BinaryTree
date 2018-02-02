'''
Inorder traversal of the binary tree without recursion
'''
import CdataS.BT.BianrySearchTree as tree

def leftnext(root, s):
    temp = root
    while temp != None:
        s.append(temp)
        temp = temp.left_child

    return s


def iwot(root):
    s = []
    final = []
    current = root
    while current != None or (len(s) > 0):
        s = leftnext(current, s)
        current = s.pop()
        final.append(current.value)
        current = current.right_child

    return final

bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
iwot(bst.root)





