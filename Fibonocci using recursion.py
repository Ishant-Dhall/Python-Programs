#Fibonocci using Recursion
def fibonocci(a):
    if a==1:
        return 0
    elif a==2:
        return 1
    else :
        return (fibonocci(a-2)+fibonocci(a-1))
a=input("Enter number upto which you want to find fiibonocci series:")
for i in range(1,a+1):
    print fibonocci(i)
