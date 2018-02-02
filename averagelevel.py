'''
Averages of Levels in Binary Tree
2
Given a non-empty binary tree, print the average value of the nodes on each level.

Examples:

Input :
    4
   / \
  2   9
 / \   \
3   5   7

Output : [4 5.5 5]
The average value of nodes on level 0 is 4,
on level 1 is 5.5, and on level 2 is 5.
Hence, print [4 5.5 5].
'''

import CdataS.BT.BianrySearchTree as tree


def avelevel(root):
    ave =[]
    q = []
    q.append(root)

    while 1:
        n = len(q)
        if n == 0:
            return ave
        temp = []
        while n >0:
            current = q.pop(0)
            temp.append(current.value)
            if current.left_child:
                q.append(current.left_child)
            if current.right_child:
                q.append((current.right_child))
            n -= 1
        ave.append(sum(temp)/float(len(temp)))



bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
avelevel(bst.root)

