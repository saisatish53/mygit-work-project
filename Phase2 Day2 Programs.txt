#Happy number
'''def happy(n):
    s=r=0
    while (n>=0):
        for i in range(0,len(str(n))+1):
            r = n%10
            s = s+r**2
            n = n//10
        return s
n = int(input("Enter a number:"))
res = n
while (res!=1 and res!=4):
    res = happy(res)
if res ==1:
    print("Happy number")
else:print("Not a happy number")'''

#Encapsulation-private
'''class encap:
    _a = 10
    c = 20

    def encapfunction(self):
        _b = 200
        print("Encap function-accessing protected")
        print(self._a+10)
obj = encap()
print(obj._a)
obj.encapfunction()
obj.c'''

#Encapsulation-protected
'''class encap:
     __a = 10
     print(__a)
     def encapfunction(self):
         print("Encap function")
         print(self.__a)
obj = encap()
obj.encapfunction()
print(obj.__a)#will throw error because
# a is private and cant be accesed outside class '''

#Encapsulation-public
'''class encap:
    a = 10
    print(a)
    def encapfunction(self):
        print("Encap function") '''

#Method overloading
'''class moverload:
    def display(self,a=None,b=None):
        print(a,b)
obj = moverload()
print("without arguments")
obj.display()
print("with arguments")
obj.display(20,30)
print("with one arguments")
obj.display(10)'''










#################################################DATA STRUCTURES##########################################


'''#SINGLE LINKED LIST
#Creating Node declaration
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singlelinkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head      #temp = first node
            while temp:
                print(temp.data,"->",end=" ")
                #temp.data means first nodes data
                temp=temp.next  #establishing link
obj = singlelinkedlist()
#Node creation-initialising
n = Node(10)    #so n.data in Node class will be 10
obj.head = n    #assigning first node as head
n1 = Node(20)
obj.head.next = n1   #next node value
n2 = Node(30)
n1.next = n2
obj.display() '''
'''


#SINGLE LINKED LIST - INSERTING AT BEGINNING
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singlelinkedlist:
    def __init__(self):
        self.head = None

    def insert_beginning(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "->", end=" ")
                temp = temp.next
obj = singlelinkedlist()
n = Node(10)
obj.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
n4 = Node(50)
n3.next = n4
print("Before inserting 100")
obj.display()
print("")
print("After inserting 100")
obj.insert_beginning(100)
obj.display()
print("")
print("After inserting 555")
obj.insert_beginning(555)
obj.display()   '''






'''
#SINGLE LINKED LIST - INSERTING AT END
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singlelinkedlist:
    def __init__(self):
        self.head = None

    def insert_end(self,data):
        ne = Node(data)
        temp=self.head
        while temp.next:
            temp = temp.next
        temp.next = ne


    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "->", end=" ")
                temp = temp.next
obj = singlelinkedlist()
n = Node(10)
obj.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
print("Before inserting 100")
obj.display()
print("")
print("After inserting 100")
obj.insert_end(100)
obj.display()
print("")   '''








'''
#SINGLE LINKED LIST - INSERTING AT A POSITION
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singlelinkedlist:
    def __init__(self):
        self.head = None

    def insert_position(self,pos,data):
        np = Node(data)
        temp=self.head
        for i in range(pos-1):
            temp = temp.next
        np.next = temp.next
        temp.next = np


    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "->", end=" ")
                temp = temp.next
obj = singlelinkedlist()
n = Node(10)
obj.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
print("Before inserting 100")
obj.display()
print("")
print("After inserting 100")
obj.insert_position(1,100)
obj.display()
print("")   '''

'''
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self,data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head

        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data,end = ' ')
            current = current.next

a_llist = LinkedList()
n = int(input("How many elements you like to ...?"))
for i in range(n):
    data = int(input("Enter data item :"))
    a_llist.append(data)
print("The linked list is ",end=" ")
a_llist.display()
'''