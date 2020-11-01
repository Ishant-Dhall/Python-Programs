# Matrix Addition
m=input("Enter the no. of rows=")
n=input("Enter the no. of columns=")
temp1=[]
list1=[]
print"List1"
for i in range(m):
    for j in range(n):
        a=input("Enter the no. you wat to enter in your matrix=")
        temp1.append(a)
    list1.append(temp1)
    temp1=[]
list2=[]
print"List2"
for i in range(m):
    for j in range(n):
        b=input("Enter the no. you wat to enter in your matrix=")
        temp1.append(b)
    list2.append(temp1)
    temp1=[]
list3=[]
for i in range(m):
    for j in range(n):
        temp1.append(0)
    list3.append(temp1)
    temp1=[]
for i in range(m):
    for j in range(n):
        list3[i][j]=list1[i][j]+list2[i][j]
print list3
        
        

        
