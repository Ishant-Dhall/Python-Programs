#Linear Search
a=[]
b=input("Enter how many element you want to enter in list:")
for i in range(0,b):
    c=input("Enter Value:")
    a.append(c)
d=input("Enter which element you want to find:")
for i in range(0,b):
    if a[i]==d:
        print "Element found at ",i+1," position..."
    continue
