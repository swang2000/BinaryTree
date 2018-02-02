'''
Iterative Method to find Height of Binary Tree
2.3
There are two conventions to define height of Binary Tree
1) Number of nodes on longest path from root to the deepest node.
2) Number of edges on longest path from root to the deepest node.

In this post, the first convention is followed. For example, height of the below tree is 3.

Example Tree
Example Tree

Recursive method to find height of Binary Tree is discussed here. How to find height without recursion? We can use level order traversal to find height without recursion. The idea is to traverse level by level. Whenever move down to a level, increment height by 1 (height is initialized as 0). Count number of nodes at each level, stop traversing when count of nodes at next level is 0.
Following is detailed algorithm to find level order traversal using queue.
'''

import CdataS.BT.BianrySearchTree as tree
def heightbyiter(root):
    if root == None:
        return 0
    q = [root]
    level = 0
    while 1:
        nodecount = len(q)
        if nodecount == 0:
            return level
        level += 1

        while nodecount > 0:
            temp_node = q.pop(0)
            if temp_node.left_child:
                q.append(temp_node.left_child)
            if temp_node.right_child:
                q.append(temp_node.right_child)
            nodecount -= 1


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
heightbyiter(bst.root)

