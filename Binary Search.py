#Binary search
def binary(a,d,b):
    e=0
    while e<b:
        beg=0
        last=b
        mid=(beg+last)/2
        if (a[mid])==d:
            value=mid
            break
        elif (a[mid])<d:
            beg=mid+1
        elif (a[mid])>d:
            last=mid-1
        e=e+1
    return value

a=[]
b=input("Enter how many element you want to enter in list:")
for i in range(0,b):
    c=input("Enter Value:")
    a.append(c)
a.sort()
d=input("Enter which element you want to find:")
e=binary(a,d,b)
print "Element Found at ",e," Position"


