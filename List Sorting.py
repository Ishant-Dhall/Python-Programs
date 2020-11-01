#List Sorting
print "THE FOLLOWING PROGRAM CHECKS WHETHER A LIST IS ARRANGED IN ASCENDING ORDER OR NOT"
def sortedornot(lst):
    li=[]
    for i in range(0:
        li[i]
    li.sort()
    if lst==li:
        return True
    else:
        return False,"The sorted list is: ",li
def main():
    x=raw_input("Enter the numbers separated by spaces: ")
    lst=x.split()
    print sortedornot(lst)
main()
