'''
Print level order traversal line by line | Set 1
2.5
Given a binary tree, print level order traversal in a way that nodes of all levels are printed in separate lines.

For example consider the following tree

          1
       /     \
      2       3
    /   \       \
   4     5       6
        /  \     /
       7    8   9

Output for above tree should be
1
2 3
4 5 6
7 8 9
'''

import CdataS.BT.BianrySearchTree as tree

def printinlevel(root):
    q =[root]
    while True:
        nodecount = len(q)
        if nodecount == 0:
            return
        a = ''
        for i in q:
            a=  a + ' ' +  str(i.value)
        print(a)
        while nodecount > 0:
            temp = q.pop(0)
            if temp.left_child:
                q.append(temp.left_child)
            if temp.right_child:
                q.append(temp.right_child)
            nodecount -= 1



bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
printinlevel(bst.root)









