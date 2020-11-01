#Sum of digits
print "THE FOLLOWING PROGRAM FINDS THE SUM OF ALL THE DIGITS OF A NUMBER"
x=input("Enter a three digit number: ")
a=(x/100)
b=(x-(x/100)*100)/10
c=(x%10)
sum=a+b+c
print "The sum of the digits of",x,"is:",sum
