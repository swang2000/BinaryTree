'''
Inorder predecessor and successor for a given key in BST
2.8
I recently encountered with a question in an interview at e-commerce company. The interviewer asked the following question:

There is BST given with root node with key part as integer only. The structure of each node is as follows:

struct Node
{
    int key;
    struct Node *left, *right ;
};
Run on IDE
You need to find the inorder successor and predecessor of a given key. In case the given key is not found in BST, then
return the two values within which this key will lie.

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.

Following is the algorithm to reach the desired result. Its a recursive method:

Input: root node, key
output: predecessor node, successor node

1. If root is NULL
      then return
2. if key is found then
    a. If its left subtree is not null
        Then predecessor will be the right most
        child of left subtree or left child itself.
    b. If its right subtree is not null
        The successor will be the left most child
        of right subtree or right child itself.
    return
3. If key is smaller then root node
        set the successor as root
        search recursively into left subtree
    else
        set the predecessor as root
        search recursively into right subtree
Following is C++ implementation of the above algorithm:
'''


def prepostnode(root, key, pre=None, post=None):
    if root == None:
        return pre, post
    else:
        if root.value > key:
            post = root.value
            pre, post = prepostnode(root.left_child, key, pre, post)
        if root.value < key:
            pre = root.value
            pre, post = prepostnode(root.right_child, key, pre, post)
        if root.value == key:
            if root.left_child:
                temp = root.left_child
                while temp.right_child:
                    temp = temp.right_child
                    pre = temp.value
            if root.right_child:
                temp = root.right_child
                while temp.left_child:
                    temp = temp.left_child
                    post = temp.value
        return pre, post

bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
prepostnode(bst.root, 2.8)
