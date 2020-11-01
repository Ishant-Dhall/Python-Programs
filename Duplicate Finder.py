#Finding Duplicates
print "THE FOLLOWING PROGRAM CHECKS FOR DUPLICATES IN A LIST AND REMOVES THEM"
n= input ("Enter the number of students in Group 2 of Computer Science: ")
print "Enter the unique Roll No of students"
list=[]
for i in range (0,n):
    list.append(input())
for j in range (0,i):
    x=list.count(list[j])
    if x>1:
        print "Duplicates found"
        print list[j],"Occured",x,"times"
        list.remove(list[j])
print "The updated list is: ",list

