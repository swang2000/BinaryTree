import math
import CdataS.Tree as Tree

##  Check if the tree is balanced
def getHeight(tNode):
    if tNode == None:
        return -1
    return max(getHeight(tNode.left_child), getHeight(tNode.right_child)) + 1


def isBalanced(tNode):
    if (tNode == None):
        return True
    heightDiff = getHeight(tNode.left_child) - getHeight(tNode.right_child)
    if (abs(heightDiff) > 1):
        return False
    else:
        return isBalanced(tNode.left_child) & isBalanced(tNode.right_child)


# Check if a tree is a binary search tree
def checkBST(tNode, min=None, max=None):
    if (tNode == None):
        return True
    if (min != None):
        if tNode.value <= min:
            return False
    if (max != None):
        if(tNode.value > max):
            return False
    if (not checkBST(tNode.left_child, min, tNode.value)) or (not checkBST(tNode.right_child, tNode.value, max)):
        return False
    return True



# figure out the successor of node as in order in a binary search tree
def inorderSucc(tNode):
    if (tNode == None):
        return None
    if (tNode.right != None):
        return leftMostChild(tNode.right)
    else:
        q = tNode
        x = q.parent
        while (x != None) & (x.left_child != q):
            q = x
            x = x.parent
            return x


def leftMostChild(tNode):
    if (tNode == None):
        return None
    while (tNode.left_chhild != None):
        tNode = tNode.left_child
    return tNode




bst = Tree.BST()
bst.insert(10)
bst.insert(8)
bst.insert(6)
bst.insert(9)
bst.insert(12)
bst.insert(23)
bst.insert(13)
bst.insert(28)
bst.preorder()

getHeight(bst.root)
isBalanced(bst.root)
checkBST(bst.root)