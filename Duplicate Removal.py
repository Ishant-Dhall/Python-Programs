#Duplicate Removal
print "THE FOLLOWING PROGRAM CHECKS FOR MULTIPLE OCCURENCES OF AN ELEMENT IN A LIST AND REMOVES ALL BUT ONE OF THEM"
def removedup(lst):
    li=[]
    for i in lst:
        li.append(i)
    for i in lst:
        c=lst.count(i)
    for j in range(1,c):
        li.remove(i)
    return "The updated list is:",li
def main():
    x=raw_input("Enter the numbers separated by spaces: ")
    lst=x.split()
    print removedup(lst)
main()
   
