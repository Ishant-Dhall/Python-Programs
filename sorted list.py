#WAP to find whether the list is sorted or not
import sys
def issorted(list1):
    for i in range(1,len(list1)):
        if list1[i]<list1[i-1]:
            return False
    return True
list1=[1,2,3,4,5,6,7,9]
if issorted(list1):
    print "yes the list is sorted"
else:
    print"No"
