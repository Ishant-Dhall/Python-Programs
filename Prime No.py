#Prime or not
print 'THE FOLLOWING PROGRAM CHECKS WHETHER A GIVEN NO IS A PRIME NO OR NOT'
x=input('Input the number: ')
count=0
if x<0: print 'This is a negative number'
elif x==1: print '1 is neither a prime nor a composite number'
else:
    for n in range (1,(x/2)+1):
        if x%n==0: count=count+1
    if (count==1):
        print 'This is a prime number'
    elif (count>1):
        print 'This is a not a prime number'
