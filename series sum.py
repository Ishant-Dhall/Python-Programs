#Series Sum
print "THE FOLLOWING PROGRAM PRINTS THE SUM OF THE SERIES x+(x**2)+(x**3)+(x**4)+........+(x**n) UPTO n TERMS"
x=input("Enter the value of x: ")
n=input("Enter the value of n: ")
sum=0
for i in  range (1,n+1):
    sum=sum+(x**i)
print "The sum of the series upto",n,"terms is: ",sum
