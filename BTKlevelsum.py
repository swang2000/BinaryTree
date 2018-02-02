'''
Binary Tree K level sum
Show Topic Tags         Samsung
Given a binary tree and a number K, the task is to find sum of tree nodes at level k. The Binary Tree s given in string form: (node-value(left-subtree)(right-subtree)).

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer K denoting level of Binary Tree for which we need sum. Next line is string which represents Binary Tree.

Output:
Print the Sum of all the elements at k level in each line.

Constraints:
1<=T<=100
1<=K<=20

Example:
Input:
1
2
(0(5(6()())(4()(9()())))(7(1()())(3()())))
Output:
14
Explaination:
The Tree from the above String will formed as:
                             0
                          /     \
                       5         7
                    /      \     /    \
                   6       4    1     3
                             \
                             9

** For More Input/Output Examples Use 'Expected Output' option **

Contributor: Saksham Raj Seth
'''


def BTKlevelsum(s, k):
    L=-1
    sum =0
    for i in range(len(s)-1):
        if s[i] =='(':
            L = L+1
        elif s[i] == ')':
            L -= 1
        if L == k and s[i+1].isdigit()==True:
            sum += int(s[i+1])
    return sum

s= '(0(5(6()())(4()(9()())))(7(1()())(3()())))'
BTKlevelsum(s, 2)




