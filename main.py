'''#Binary Search Tree-Delete
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
#a new node with the given key
def insert(node,key):
    if node is None:
        return  Node(key)
    if key < node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def minValueNode(node):
    current= node
    while(current.left is not None):
        current = current.left
    return current
def deleteNode(root,key):
    #Base class
    if root is None:
        return root
    #key<root , it lies in left subtree
    if key < root.key:
        root.left=deleteNode(root.left,key)
    elif (key > root.key):
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return  temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        #smallest in the right subtree
        temp = minValueNode(root.right)
        #copy the inorder's successor's content to this node
        root.key = temp.key
        #Delete the inorder's successor
        root.right = deleteNode(root.right,temp.key)
    return root
root = None
root = insert(root,50)
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)
root = insert(root,70)
root = insert(root,60)
root = insert(root,80)
print("Inorder traversal of the given tree ")
inorder(root)
print("\nDelete node 20")
root = deleteNode(root,20)
print("Inorder traversal of the modified tree ")
inorder(root)
print("\nDelete node 30")
root = deleteNode(root,30)
print("Inorder traversal of the modified tree ")
inorder(root)
print("\nDelete node 50")
root = deleteNode(root,50)
print("Inorder traversal of the modified tree ")
inorder(root)   '''
##############################################################################################
'''#Graph Implementation

#import dictionary for graph
from collections import defaultdict
#ADD EDGE TO GRAPG - FUNCTION
graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)

#FUNCTION DESCRIPTION
def generate_edges(graph):
    edges = []
    #for each node in graph
    for node in graph:
        #for each neighbour node of a single node
        for neighbour in graph[node]:
            #if edge exists then append
            edges.append((node,neighbour))
    return edges

#Declaring-graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')
#PRINTING GRAPH
print(generate_edges(graph))    '''
##############################################################################################

'''#ADJACENCY MATRIX
class Graph(object):
    #Initialize the matrix
    def __init__(self,size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
    #Add edges
    def add_edge(self,v1,v2):
        if v1 == v2:
            print("Same vertex %d and %d" %(v1,v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    #Remove edges
    def remove_edge(self,v1,v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" %(v1,v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size
    #Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print("{:4}".format(val))
            print()
def main():
    g = Graph(5)
    g.add_edge(0,1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()
if __name__ == "__main__":
    main()
'''
##############################################################################################
'''#BFS
graph = {'5':['3','7'],
         '3':['2','4'],
         '7':['8'],
         '2':[],
         '4':['8'],
         '8':[]
    }
#BFS-we use Queue
visited = []
queue = []
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m,end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs(visited,graph,'5')  '''

#DFS
#Using dictionart to act as an adjacency list
graph = {'5':['3','7'],
         '3':['2','4'],
         '7':['8'],
         '2':[],
         '4':['8'],
         '8':[]
    }
visited = set()     
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

dfs(visited,graph,'5')