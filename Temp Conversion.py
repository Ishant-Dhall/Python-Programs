#Temperature Conversion
print "The following Program converts temperature from degree celcius to degree fahrenheit and vice versa."
print '''Enter your choice
Enter 1 for celcius to fahrenheit conversion
Enter 2 for fahrenheit to celcius conversion'''
n=input("")
def cel_fah(x):
    f=(9/5.0)*x+32
    print x,"degree celcius =",f,"degree fahrenheit"
def fah_cel(x):
    c=(5*(x-32))/9.0
    print x,"degree fahrenheit =",c,"degree celcius "
if n==1:
    x=input("Enter the temperature in degree celcius: ")
    cel_fah(x)
elif n==2:
    x=input("Enter the temperature in degree fahrenheit: ")
    fah_cel(x)
    
