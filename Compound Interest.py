#Compound Interest
print "THE FOLLOWING PROGRAM CALCULATES COMPOUND INTEREST"
p=input("Enter the principal amount: ")
r=input("Enter the interest rate: ")
t=input("Enter the time period(In years): ")
a=p*(1+r/100.0)**t
print "The amount payable after",t,"years is: ",a
        
