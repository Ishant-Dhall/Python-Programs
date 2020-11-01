#Sales Commission
print "THE FOLLOWING PROGRAM CALCULATES THE SALES COMMISSION FOR SALES OBTAINED BY A SALES PERSON"
x=input("Enter the sales obtained by the sales person: ")
if (x>=35001): sales_comm=(0.25*x)
elif (x>=25001)&(x<=35000): sales_comm=(0.20*x)
elif (x>=20001)&(x<=25000): sales_comm=(0.15*x)
elif (x>=15001)&(x<=20000): sales_comm=(0.12*x)
elif (x>=10001)&(x<=15000): sales_comm=(0.1*x)
elif (x>=5001)&(x<=10000): sales_comm=(0.05*x)
elif (x>=0)&(x<=5000): sales_comm=0
else: print "Not a valid input"
print "Sales Commission on Rs",x,"=",sales_comm
