#Fibonacci Series
fb=0
fb1=1
a=input("Enter how many Fibonacci series you want to find:")
if a==1:
    print fb
elif a==2:
    print fb,fb1
elif a>2:
    print fb,"\n",fb1
    for i in range(2,a):
        fb2=fb+fb1
        print fb2
        fb=fb1
        fb1=fb2
print "Fibonnaci series created..."
    
        
