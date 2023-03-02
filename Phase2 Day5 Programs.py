'''class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

node1 = BinaryTreeNode(50)
node2 = BinaryTreeNode(20)
node3 = BinaryTreeNode(45)
node4 = BinaryTreeNode(11)
node5 = BinaryTreeNode(15)
node6 = BinaryTreeNode(30)
node7 = BinaryTreeNode(78)

node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7

#                           50
#               ____________|______________
#              |                          |
#              20                         45
#        _______|_______            _______|_______
#        |              |           |              |
#        11             15          30             78

print("Root node is",node1.data)
print("Left child of root node is",node1.leftChild.data)
print("Right child of root node is",node1.rightChild.data)
print("Node is",node2.data)
print(node1.rightChild.leftChild.data)  '''
#####################################################################################
'''
#Inorder traversal - example 1:
#                           A
#               ____________|______________
#              |                           |
#              B                           C
#        _______|_______            _______|_______
#        |              |           |              |
#        D              E           F              G
#    Inorder traversal : D,B,E,A,F,C,G  (Applying LDR)

#Inorder traversal - example 2:
#                           15
#               ____________|______________
#               |                          |
#               24                         54
#           ____|                  _______|_______
#          |                      |              |
#           35                    62             13
#    Inorder traversal : 35,24,15,62,54,13  (Applying LDR)'''
#####################################################################################
'''#Preorder traversal - example-1:
#                           45
#                           / \ 
#                          /   \ 
#                         25    75
#                         / \   
#                        /   \ 
#                       15    35
#    Preorder traversal :45,25,15,35,75 


#Preorder traversal - example-2:
#                           (1)
#                           / \ 
#                          /   \ 
#                         /     \ 
#                        (2)    (3)
#                        / \     /\ 
#                       /   \   /  \ 
#                     (4)  (5) (6)  (7)
#                          /         /\ 
#                         /         /  \ 
#                        (8)       (9) (10)
#    Preorder traversal :1 2 4 5 8 3 6 7 9 10
#   Inorder traversal  : 4 2 8 5 1 6 3 9 7 10'''
#####################################################################################
'''
#                           (1)
#                           / \ 
#                          /   \ 
#                         /     \ 
#                        (2)    (3)
#                        / \     /\ 
#                       /   \   /  \ 
#                     (4)  (5) (6)  (7)
#
#   Preorder: 1,2,4,5,3,6,7
#   Inorder : 4,2,5,1,6,3,7
#   Postorder: 4,5,2,6,7,3,1    '''
#####################################################################################
'''#print Preorder,Inorder,Postorder
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
def printInorder(root):
    if root:
        #First recur on left child
        printInorder(root.left)
        #then print the data of node
        print(root.val,end = " ")
        #now recur on right child
        printInorder(root.right)
#FUNCTION-POSTORDER
def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)
        # now recur on right child
        printPostorder(root.right)
        # now print the data of node
        print(root.val, end=" ")
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val, end=" ")
        # Then recur on left child
        printPreorder(root.left)
        # now recur on right child
        printPreorder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("PREORDER:")
printPreorder(root)
print()
print("INORDER:")
printInorder(root)
print()
print("POSTORDER:")
printPostorder(root)'''
#####################################################################################
'''#BST-INSERT
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
#a new node with the given key
def insert(root,key):
    if root is None:
        return  Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)
    return root
#Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
#                 (1)
#                 / \ 
#                /   \ 
#               /     \ 
#              (2)    (3)
#              / \     /\ 
#             /   \   /  \ 
#           (4)  (5) (6)  (7)
r = Node(50)
r = insert(r,30)
r = insert(r,20)
r = insert(r,40)
r = insert(r,70)
r = insert(r,60)
r = insert(r,80)
inorder(r)  '''