#Series 1+ 1/1**2+ 1/2**2+ 1/3**2+......+1/n**2
sum=1
n= input("Enter the value of n: ")
for i in range (1,n+1):
    sum=sum+(1.0/i**2)
print "The sum is: ",sum
