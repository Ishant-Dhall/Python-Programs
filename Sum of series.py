#Sum of Series
a=input("Enter Number upto which you want to find sum of series:")
Sum=0
b=1
def fac(b):
    fact=1
    for j in range(1,b+1):
        fact=fact*j
    return fact

while b<=a:
    if a%2==0:
        c=fac(b)
        Sum=Sum-(1.0/c)
    else:
        c=fac(b)
        Sum=Sum+(1.0/c)
    b=b+1
print "Sum of series is:",Sum
