#Finding Element in a list
print "THE FOLLOWING PROGRAM SEARCHES FOR AN ELEMENT IN A LIST"
list=['January','February','March',
      'April','May','June',
      'July','August','September',
      'October','November','December']
str=raw_input("Enter the element you want to find and remove: ")
for i in range (0,len(list)):
    if list[i]==str:
        print "Element found and removed"
        list.remove(str)
        break
else: print '''Element is not present in the list
The list remains unchanged'''
print "The updated list is: ",list

