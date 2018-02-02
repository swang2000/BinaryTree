'''
Print Postorder traversal from given Inorder and Preorder traversals
3.9
Given Inorder and Preorder traversals of a binary tree, print Postorder traversal.

Example:

Input:
Inorder traversal in[] = {4, 2, 5, 1, 3, 6}
Preorder traversal pre[] = {1, 2, 4, 5, 3, 6}

Output:
Postorder traversal is {4, 5, 2, 6, 3, 1}
Trversals in the above example represents following tree

         1
      /
     2       3
   /
  4     5      6
'''

def search(a, y):
    for i, x in enumerate(a):
        if x == y:
            return i
    return -1



def printpostorder(ino, pre, a=[]):
    i = search(ino, pre[0])
    if i != 0:
        printpostorder(ino[:i], pre[1:], a)
    if i != len(ino)-1:
        printpostorder(ino[(i+1):], pre[(i+1):], a)
    a.append(ino[i])
    return a


ino = [4, 2, 5, 1, 3, 6]
pre = [1, 2, 4, 5, 3, 6]
printpostorder(ino, pre)



