'''
Add a new node into the Binary Search Tree (BST)


    def insert(self, v):
    if self.root:
        self.root.insert(v)
    else:
        self.root = Node(v)



    def insert(self, v):
        if self.value < v:
            if self.right_child:
                self.right_child.insert(v)
            else:
                self.right_child = Node(v)
        else:
            if self.left_child:
                self.left_child.insert(v)
            else:
                self.left_child = Node(v)



The scenarios of deleting a node in a binary search tree

Case 1 - Val is the root value
Case 2 - empty tree
Case 3 - cannot find the val in the tree
Case 4 if the currentNode only has the left_child
Case 5 if the currentNode only has the right_child
Case 6 if the currentNode has both left_child and right_child


1) Node to be deleted is leaf: Simply remove from the tree.

              50                            50
           /     \         delete(20)      /   \
          30      70       --------->    30     70
         /  \    /  \                     \    /  \
       20   40  60   80                   40  60   80
2) Node to be deleted has only one child: Copy the child to the node and delete the child

              50                            50
           /     \         delete(30)      /   \
          30      70       --------->    40     70
            \    /  \                          /  \
            40  60   80                       60   80
3) Node to be deleted has two children: Find inorder successor of the node. Copy contents of the inorder successor to the node and delete the inorder successor. Note that inorder predecessor can also be used.

              50                            60
           /     \         delete(50)      /   \
          40      70       --------->    40    70
                 /  \                            \
                60   80                           80




'''

class Node:
    def __init__(self, v):
        self.value = v
        self.left_child = None
        self.right_child = None

    def get(self):
        return self.value

    def set(self, v):
        self.value = v

    def get_children(self):
        children = []
        if (self.left_child != None):
            children.append(self.left_child)
        if (self.right_child != None):
            children.append(self.right_child)

    def insert(self, val):
        if self.value <= val:
            if (self.right_child):
                return self.right_child.insert(val)
            else:
                self.right_child = Node(val)
                return True
        else:
            if (self.left_child):
                return self.left_child.insert(val)
            else:
                self.left_child = Node(val)
                return True



    def find(self, val):
        if self.value == val:
            return True
        elif self.value > val:
            if self.left_child:
                self.left_child.find(val)
            else:
                return False
        else:
            if self.right_child:
                self.right_child.find(val)
            else:
                return False

    # def getHeight(self):
    #     if self == None:
    #         return
    #     return max(self.left_child.getHeight(), self.right_child.getHeight()) + 1




    def preorder(self):
        print(str(self.value))
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(str(self.value))

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(str(self.value))
        if self.right_child:
            self.right_child.inorder()

    def depth(self):
        if self == None:
            return 0
        if self.left_child == None and self.right_child:
            return self.right_child.depth() + 1
        elif self.right_child == None and self.left_child:
            return self.left_child.depth() + 1
        elif self.left_child and self.right_child:
            return max(self.left_child.depth(), self.right_child.depth()) + 1
        else:
            return 1


class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            self.root.insert(val)
        else:
            self.root = Node(val)



    def find(self, val):
        if self.root:
            self.root.find(val)
        else:
            return False

    def preorder(self):
        print('Preorder Print')
        if self.root:
            self.root.preorder()
        else:
            print('Tree is empty')

    def postorder(self):
        print('Postorder Print')
        if self.root:
            self.root.postorder()
        else:
            print('Tree is empty')

    def inorder(self):
        print('Inorder Print')
        if self.root:
            self.root.inorder()
        else:
            print('Tree is empty')

    def delete(self, val):
        # Case 1 - Val is the root value
        if self.root.value == val:
            # 4 sub-cases in this category based on the children
            if self.root.left_child and self.root.right_child is None:
                self.root = self.root.left_child
            elif self.root.right_child and self.root.left_child is None:
                self.root = self.root.left_child
            elif self.root.left_child is None and self.root.right_child is None:
                self.root = None
            else:
                parentNode = self.root
                currentNode = self.root.left_child
                if currentNode.right_child is None:
                    self.root = currentNode
                else:
                    while currentNode.right_child:
                        parentNode = currentNode
                        currentNode = currentNode.right_child

                    self.root.value = currentNode.value
                    if currentNode.left_child:
                        parentNode.right_child = currentNode.left_child
                    else:
                        parentNode.right_child = None
        else:
            # Case 2 - empty tree
            if self.root is None:
                self.root = None

            parentNode = None
            currentNode = self.root

            while currentNode.value != val:
                parentNode = currentNode
                if (val > currentNode.value) & (currentNode.right_child is not None):
                    currentNode = currentNode.right_child
                if (val < currentNode.value) & (currentNode.left_child is not None):
                    currentNode = currentNode.left_child
                    # Case 3 - cannot find the val in the tree
            if currentNode.value != val:
                return False

                # Case 4 if the currentNode only has the left_child
            if currentNode.value == val and (currentNode.left_child is not None) and (currentNode.right_child is None):
                if parentNode.value > currentNode.left_child.value:
                    parentNode.left_child = currentNode.left_child
                else:
                    parentNode.right_child = currentNode.left_child

                    # Case 5 if the currentNode only has the right_child
            if currentNode.value == val and (currentNode.left_child is None) and (currentNode.right_child is not None):
                if parentNode.value > currentNode.right_child.value:
                    parentNode.left_child = currentNode.right_child
                else:
                    parentNode.right_child = currentNode.right_child

                    # Case 6 if the currentNode only has both left_child and right_child
            if currentNode.value == val and (currentNode.left_child is not None) and (currentNode.right_child is not None):
                delNodeparent = currentNode
                delNode = currentNode.left_child
                while (delNode.right_child is not None):
                    delNodeparent = delNode
                    delNode = delNode.right_child

                currentNode.value = delNode.value
                if (delNode.left_child is not None):
                    currentNode.left_child = delNode.left_child
                else:
                    currentNode.left_child = None



    def height(self):
        if self.root == None:
            return 0
        return max(self.root.left_child.depth(), self.root.right_child.depth()) + 1

bst = BST()
bst.insert(2)
bst.insert(3)
bst.insert(1)
bst.insert(5)
