#Compound Interest using Simple Interest
print "THE FOLLOWING PROGRAM CALCULATES COMPOUND INTEREST USING THE FORMULA OF SIMPLE INTEREST"
p=input("Enter the principal amount: ")
r=input("Enter the interest rate: ")
t=input("Enter the time period(In years): ")
for n in range (1,t+1):
    i=(p*r)/100.0
    a=p+i
    p=a
print "The amount payable after",t,"years is: ",a
        
