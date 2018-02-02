'''
Populate Inorder Successor for all nodes
3.3
Given a Binary Tree where each node has following structure, write a function to populate next pointer for all nodes.
The next pointer for every node should be set to point to inorder successor.

struct node
{
  int data;
  struct node* left;
  struct node* right;
  struct node* next;
}
'''

import CdataS.BT.BianrySearchTree as tree
class snode:
    def __init__(self, s):
        self.value = s
        self.left = None
        self.right = None
        self.next = None

    def insert(self, a):
        if self == None:
            self = self.snode(a)
        if self.value > a:
            if self.left:
                return self.left.insert(a)
            else:
                self.left = snode(a)

        else:
            if self.right:
                return self.right.insert(a)
            else:
                self.right = snode(a)

# class BT():
#     def __init__(self):
#         self.root = None
#
#     def insert(self, a):
#         if self.root:
#             self.root.insert(a)
#         else:
#             self.root = snode(a)


def inordersuc(root, next =None):
    if root:
        inordersuc(root.right, next)
        root.next = next
        next = root
        inordersuc(root.left, next)




s = snode(5)
#s.insert(5)
s.insert(3)
s.insert(2)
s.insert(2.5)
s.insert(4)
s.insert(8)
s.insert(6)

m = inordersuc(s)
