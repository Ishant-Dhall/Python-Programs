#HCF (Highest Common Factor)
print "THE FOLLOWING PROGRAM FINDS THE HCF OF TWO NUMBERS"
x=input("Input the first number: ")
y=input("Input the second number: ")

def hcf(x,y):
    if x<y: minim=x
    else: minim=y
    return minim
minim=hcf(x,y)
for i in range (1,minim+1):
    if (x%i==0) & (y%i==0):
        hcf=i
    continue
print "The hcf of",x,"&",y,"is: ",hcf

