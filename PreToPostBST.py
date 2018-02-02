'''
Preorder to Postorder
Show Topic Tags           Amazon
Given an array representing preorder traversal of BST, print its postorder traversal.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the size of array.
The second line of each test case contains N input A[i].

Output:
Postorder traversal of the given preorder traversal is printed. Otherwise 'NO' is printed.

Constraints:
1 <=T<= 100
1 <= N <= 1000
1 <= arr[i] <= 1000

Example:

Input:
3
5
40 30 35 80 100
8
40 30 32 35 80 90 100 120
8
7  9 6 1 4 2 3 40

Output:
35 30 100 80 40
35 32 30 120 100 90 80 40
NO

** For More Input/Output Examples Use 'Expected Output' option **
'''

def preTopost(a):
    s = []
    out =[]
    sout = []
    root = -2**31
    oldroot = root
    for value in a:
        if value < root:
            return False
        flag = False
        while len(s) >0 and (s[-1] < value):
            oldroot = root
            root = s.pop()
            flag = True
        s.append(value)
        while (len(out)>0) and out[-1] < root and (oldroot > -2**31) and flag:
            sout.append(out.pop())
        out.append(value)
    while (len(out) > 0):
        sout.append(out.pop())
    return sout


b = [40, 30, 25, 28, 32, 35, 80, 90, 100, 120]
preTopost(b)