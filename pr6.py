size=int(input("size:"))
l=[]
for i in range(size):
     ele=int(input("element:"))
     l.append(ele)
print(l)
prod=1
for j in l:
     prod=prod*j
sum=0
for k in l:
     sum=sum+k

if(prod<750):
     print("prod=",prod)
else:
     print("sum=", sum)
