'''
Sum of k smallest elements in BST
Show Topic Tags
Given Binary Search Tree. The task is to find sum of all elements smaller than and equal to Kth smallest element.
Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow.
Each test case consists of three lines.
First line of each test case consist of integer N, denoting the number of elements in a BST.
Second line of each test case consists of N space separated integers denoting the elements in the BST.
Third line of each test case consists of an integer K, denoting the Kth smallest elements.

Output:
It should be single line output, Print the respective output in the respective line.

Constraints:
1<=T<=100
1<=N<=50
1<=K<=N

Example:
Input:
1
7
20 8 4 12 10 14 22
3
Output:
22
Explanation:
The tree for above input will look like this:
          20
        /     \
       8     22
     /     \
    4     12
         /     \
        10    14
Sum of 3 smallest elements are: 4 + 8 + 10 = 22

** For More Input/Output Examples Use 'Expected Output' option **

Contributor: Saksham Raj Seth
'''

import CdataS.BT.BianrySearchTree as Tree
def sumKsmall(root, a=[]):
    if root != None:
        sumKsmall(root.left_child, a)
        a.append(root.value)
        sumKsmall(root.right_child, a)
        return a

bst = Tree.BST()
bst.insert(2)
bst.insert(3)
bst.insert(1)
bst.insert(5)
b =sumKsmall(bst.root)
k = 3
sum(b[0:k])