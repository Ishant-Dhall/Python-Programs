#Armstrong number
print "THE FOLLOWING PROGRAM CHECKS WHETHER A GIVEN NUMBER IS AN ARMSTRONG NUMBER OR NOT"
x=input("Enter a three digit number: ")
a=(x/100)
b=(x-(x/100)*100)/10
c=(x%10)
if ((a**3)+(b**3)+(c**3)==x): print "This is an Armstrong Number"
else: print "This is not an Armstrong Number"
