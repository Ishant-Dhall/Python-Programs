#For removing the duplicates from the list
import sys
def duplicate(list1):
    list2=[]
    n=len(list1)
    for i in list1:
        list2.append(i)
    for i in range(n):
        for j in range(i+1,n):
            if list1[i]==list1[j]:
                list2.remove(list1[i])
                break
    return list2
list1=[]
print"1.To append numbers in the list"
print"2.To append characters in the list"
ch=input("Enter your choice=")
n=input("Enter the no. of elements=")
for i in range(n):
    if ch==1:
        a=raw_input("Enter the element=")
    elif ch==2:
        a=raw_input("Enter the element=")
    else:
        print"Invalid choice!"
        sys.exit()
    list1.append(a)
list3=duplicate(list1)
print"After removing the duplicates from the list,the list is as follows:\n",list3
