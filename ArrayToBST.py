'''
Array to BST
Show Topic Tags          Amazon    Cisco    VMWare
Given a sorted array. Write a program that creates a Balanced Binary Search Tree using array elements. If there are n
elements in array, then floor(n/2)'th element should be chosen as root and same should be followed recursively.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the size of array.
The second line of each test case contains N input A[].

Output:

Print the preorder traversal of constructed BST.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 1000
1 ≤ A[] ≤ 10000

Example:

Input:
1
7
7 6 5 4 3 2 1

Output:
4 6 7 5 2 3 1
'''
import CdataS.BT.BianrySearchTree as Tree
def arrayToBst(a):
    n = len(a)
    if n>=1:
        node = Tree.Node(a[n//2])
        node.left_child= arrayToBst(a[(n//2)+1:])
        node.right_child = arrayToBst(a[:(n//2)])
        return node


a = [7, 6,5, 4, 3, 2, 1]
b = arrayToBst(a)