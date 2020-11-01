#LCM
print "THE FOLLOWING PROGRAM PRINTS THE LCM OF TWO NUMBERS"
x=input("Input the first number: ")
y=input("Input the second number: ")
def lcm(x,y):
    if x>y: maxim=x
    else: maxim=y
    return maxim
maxim=lcm(x,y)
while(1):
    if (maxim%x==0) & (maxim%y==0):
        lcm=maxim
        break
    else:
        maxim=maxim+1
        continue
print "The LCM of",x,"&",y,"is: ",lcm
