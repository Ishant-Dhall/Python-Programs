#Kite Pattern
x=input("How many rows do you want in kite pattern(Odd number only): ")
k=(x+1)/2
for i in range(1,x+1):
    j=abs(k-i)
    if (i<=k): print " "*j,"* "*i
    elif (i>k): print " "*j,"* "*(x+1-i)
                
