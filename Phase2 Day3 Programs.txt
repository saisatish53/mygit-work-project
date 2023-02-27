'''
#while creating LL we gonna do it in ascending order
#one program multiple concepts :)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        if not temp:
            print("List is empty")
            return
        else:
            print("Start:",end = " ")
        while temp:
            print(temp.data , end =" ->")
            temp = temp.next
        print("end.")
    def insert(self,data):
        new_node = Node(data)
        
        #If the linked list is empty
        if self.head is None:
            self.head = new_node
        #If the data is smaller than the head
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            #Locate the node before the insertion point
            current = self.head
            while current.next and new_node.data > current.next.data:
                current = current.next
            #Insertion
            new_node.next = current.next
            current.next = new_node
    def delete(self,key):
            #If the list is empty
            if self.head is None:
                print("Deletion error : The list is empty")
                return
            #If the key is in head
            if self.head.data == key:
                self.head = self.head.next
                return
            #Find position of first occurence of the
            current = self.head
            while current:
                if current.data == key:
                    break
                previous = current
                current = current.next
            #If the key was not found
            if current is None:
                print("Deletion error : Key not found")
            else:
                previous.next = current.next
#__name__ is python special variable
if __name__ == "__main__":
    #Create an object
    LL = LinkedList()
    print(" ")
    #Insert some nodes
    LL.insert(10)
    LL.insert(12)
    LL.insert(8)
    LL.insert(11)
    LL.insert(10)


    LL.printList()
    LL.delete(12)
    LL.delete(8)
    LL.delete(10)
    LL.printList()  '''

#----------------------------------------------------------------------------------------------------------------
'''#Double Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
class dll:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"<-->",end = " ")
                temp = temp.next

l = dll()
n1 = Node(100)
l.head = n1
n2 = Node(200)
n2.previous = n1
n1.next = n2
l.display()'''
#-----------------------------------------------------------------------------
'''
#Double Linked List insert at start
class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
class dll:
    def __init__(self):
        self.head = None
    def insert_start(self):
        n = Node(300)
        temp = self.head
        temp.prev = n
        n.next = temp
        self.head = n

    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "<-->", end=" ")
                temp = temp.next
l = dll()
n1 = Node(100)
l.head = n1
n2 = Node(200)
n2.previous = n1
n1.next = n2
l.insert_start()
l.display() '''
#--------------------------------------------------------------------------------

'''#Double Linked List insert at end
class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
class dll:
    def __init__(self):
        self.head = None
    def insert_end(self):
        n = Node(300)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = n
        n.previous = temp

    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "<-->", end=" ")
                temp = temp.next
l = dll()
n1 = Node(100)
l.head = n1
n2 = Node(200)
n2.previous = n1
n1.next = n2
l.insert_end()
l.display() '''
#--------------------------------------------------------------------------------
'''#Double Linked List insert at position
class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
class dll:
    def __init__(self):
        self.head = None
    def insert_pos(self,pos):
        n = Node(400)
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        n.previous = temp
        n.next = temp.next
        temp.next.previous = n
        temp.next = n

    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "<-->", end=" ")
                temp = temp.next
l = dll()
n1 = Node(100)
l.head = n1
n2 = Node(200)
n2.previous = n1
n1.next = n2
n3 = Node(300)
n3.previous = n2
n2.next = n3
l.insert_pos(2)
l.display() '''
#--------------------------------------------------------------------------------
'''
#Double Linked List-Deleting at the beginning
class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
class doublelinkedlist:
    def __init__(self):
        self.head = None
    def delete_beginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "<-->", end=" ")
                temp = temp.next
l = doublelinkedlist()
n1 = Node(100)
l.head = n1
n2 = Node(200)
n2.previous = n1
n1.next = n2
l.delete_beginning()
l.display() '''
#--------------------------------------------------------------------------------
'''
#Double Linked List-Deleting at the end
class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
class doublelinkedlist:
    def __init__(self):
        self.head = None
    def delete_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not  None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "<-->", end=" ")
                temp = temp.next

l = doublelinkedlist()
n1 = Node(100)
l.head = n1
n2 = Node(200)
n2.previous = n1
n1.next = n2
l.delete_end()
l.display()'''
#--------------------------------------------------------------------------------
'''
#Double Linked List-Deleting at the given position
class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
class doublelinkedlist:
    def __init__(self):
        self.head = None
    def delete_position(self,pos):
        temp = self.head.next
        prev = self.head
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None

    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "<-->", end=" ")
                temp = temp.next

l = doublelinkedlist()
n1 = Node(100)
l.head = n1
n2 = Node(200)
n2.previous = n1
n1.next = n2
n3 = Node(300)
n3.previous = n2
n2.next = n3
l.delete_position(1)
l.display()  '''
#-------------------------------------------------------------------------------

'''#Circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CreateList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next  = self.head
    #adding node at the end of LL
    def add(self,data):
        newNode = Node(data)
    #Is empty?
        if self.head.data is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
            #It is CLl,so tail will point to head
            self.tail.next = self.head

    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        else:
            print("Nodes of the linked list:")
            print(current.data,"-->")
            while (current.next != self.head):
                current = current.next
                print(current.data,"-->")

class CircularLinkedList:
    c1 = CreateList()
    c1.add("S")
    c1.add("M")
    c1.add("I")
    c1.add("L")
    c1.add("E")
    c1.display()	'''


