#Class Report
a=[0 for i in range(0,3)]
for i in range(0,3):
    c=input("Enter Marks out of 75:")
    a[i]=c
if (a[0]>30)&(a[1]>30)&(a[2]>30):
    Sum=0
    for i in range(0,3):
        Sum=Sum+a[i]
    per=(Sum/225.0)*100.0
    print "Your Sum is:",Sum,"\nPercentage is:",per
    if per>=80:
        print "Your Grade is:A"
    elif (per>=70)&(per<80):
        print "Your Grade is:B"
    
    elif (per>=60)&(per<70):
        print "Your Grade is:C"
    elif (per>=50)&(per<60):
        print "Your Grade is:D"
    elif per<40:
        print "Your Grade is:E"
else:
    print "You got fail..."
    
    
    
