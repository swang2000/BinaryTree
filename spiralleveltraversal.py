'''
Level order traversal in spiral form
2.8
Write a function to print spiral order traversal of a tree. For below tree, function should print 1, 2, 3, 4, 5, 6, 7.

spiral_order

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
'''


import CdataS.BT.BianrySearchTree as tree

def spiral(root):
    flag = True
    sl = []
    sr = []
    a = []
    temp = root
    sl.append(temp)
    while len(sl) > 0 or len(sr) > 0:
        while len(sl) > 0:
            temp = sl.pop(-1)
            a.append(temp.value)
            if temp.right_child:
                sr.append(temp.right_child)
            if temp.left_child:
                sr.append(temp.left_child)
        while len(sr) > 0:
            temp = sr.pop(-1)
            a.append(temp.value)
            if temp.left_child:
                sl.append(temp.left_child)
            if temp.right_child:
                sl.append(temp.right_child)
    return a


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
spiral(bst.root)



'''
The following code works, but has some bugs
def spiral(root):
    flag = True
    sl = []
    sr = []
    a = []
    temp = root
    sl.append(temp)
    a.append(temp.value)
    while 1:
        if flag:
            nodecount = len(sl)
        else:
            nodecount = len(sr)
        if nodecount == 0:
            return a

        while nodecount > 0 and temp:
            if flag:
                temp = sl.pop(-1)
                if temp.left_child:
                    sr.append(temp.left_child)
                    a.append(temp.left_child.value)
                if temp.right_child:
                    sr.append(temp.right_child)
                    a.append(temp.right_child.value)
            else:
                temp = sr.pop(-1)
                if temp.right_child:
                    sl.append(temp.right_child)
                    a.append(temp.right_child.value)
                if temp.left_child:
                    sl.append(temp.left_child)
                    a.append(temp.left_child.value)
            nodecount -= 1
        flag = not flag

'''
