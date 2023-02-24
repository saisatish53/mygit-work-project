'''l = [1,2,3]
r = map(lambda x:x+x,l)
print(list(r))
res = map(lambda n:pow(n,2),l)
print(list(res))
name = "Shiva"
(lambda name:print(name))(name)
-----------------------------------------------------------
l = []
for i in range(1,16):
    if i%2==0:
        l.append(i)
print(l)
res = map(lambda res:pow(res,1/2),l)
print(list(res))

------------------------------------------------------------
import abc from ABC
class abstractdemo(ABC):
    @abstractmethod
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
class demo(abstractdemo):
    def display(self):
        print("Abstraction method")
    def show(self):
        print("2nd function")
obj = demo()
obj.display()
obj.show()
------------------------------------------------------------
#                                    INHERITANCE
class parent:
    def display(self):
        print("Parent class")
class child(parent):
    def show(self):
        print("Child class")

c = child()
c.display()
c.show()
------------------------------------------------------------

#single inheritance
class A:
    n = 30
class B(A):
    def calc(self):
        print(self.n+70)
obj = B()
obj.calc()
------------------------------------------------------------
#multiple inheritance
class mom:
    def mdisplay(self):
        print("Mom class")
class dad:
    def ddisplay(self):
        print("Dad class")
class child(mom,dad):
    def cdisplay(self):
        print("Child class")
c1 = child()
c1.mdisplay()
c1.cdisplay()
c1.ddisplay()
------------------------------------------------------------
#multilevel inheritance
class grandparent:
    def display(self):
        print("Grandparents class")
class parent(grandparent):
    def show(self):
        print("Parents class")
class child(parent):
    def printing(self):
        print("Child class")
c1 = child()
c1.display()
c1.show()
c1.printing()
------------------------------------------------------------
#hierarchical inheritance
class parent:
    def pdisplay(self):
        print("Parent class")
class child1(parent):
    def c1show(self):
        print("Child 1 class")
class child2(parent):
    def c2show(self):
        print("Child 2 class")
c1 = child1()
c1.c1show()
c1.pdisplay()
c2 = child2()
c2.c2show()
c2.pdisplay()
------------------------------------------------------------
#hybrid inheritance

#                       parent
#                 _________|_________
#                |                   |
#              Kid1                Kid2
#          _____|____             _____|____
#         |         |            |          |
#       Child1     Child2      Child3       Child4
class parent:
    def pdisplay(self):
        print("Parents class")
class kid1(parent):
    def k1show(self):
        print("Kid1 class")
class kid2(parent):
    def k2show(self):
        print("Kid2 class")
class child1(kid1):
    def c1show(self):
        print("Child1 class")
class child2(kid1):
    def c2show(self):
        p*i+t("Child2 class")
class child3(kid2):
    def c3show(self):
        print("Child3 class")
class child4(kid2):
    def c4show(self):
        print("Child4 class")
c1 = child1()
c1.c1show()
c1.k1show()
c1.pdisplay()
c2 = child2()
c2.k1show()
c2.pdisplay()
c2.c2show()
c3 = child3()
c3.pdisplay()
c3.k2show()
c3.c3show()
c4 = child4()
c4.k2show()
c4.pdisplay()
c4.c4show()
------------------------------------------------------------'''
'''n=int(input("Enter :"))
def happy(b):
    l = []
    for i in str(b):
       l.append(int(i))
    sum = 0
    for j in l:
         sq = j*j
         sum =sum+sq
    return sum
x=happy(n)
if x!= 1:
    happy(x)
else:
    print("Its a happy number")'''

n=int(input("Enter :"))
while (n>1):
    s = 0
    for i in range(0,len(str(n))):
        r = n%10
        s = s+r**2
        n = n//10
    n = s
if n ==1:
    print("Happy number")
else:
    print("Not happy number")