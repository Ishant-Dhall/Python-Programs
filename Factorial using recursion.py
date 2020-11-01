#factorial using recursion
def fact(a):
    if (a==0)|(a==1):
        return 1
    else:
        return a*fact(a-1)

a=input("Enter number whose factorial you want to find:")
b=fact(a)
print "Factorial of ",a," is:",b 
