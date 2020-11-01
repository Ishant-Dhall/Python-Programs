#Sum of the series 1+ 1/1!- 2/2!+ 3/3!- ...... n/n!
x=input("How many terms do you want to add: ")
sum=1.0
factorial=1
def fact(j):
    fact=1
    for j in range(j,1,-1):
        fact=fact*j
    return fact
for i in range (1,x):
    sum=sum+((-1.0)**(i+1)*i)/fact(i)
print "The sum upto",x,"terms = ",sum



