#Simple Interest and Compound Interest using functions
def simple_int(p,r,t):
    try:
        if p=="": p= None
        print p
        p=float(p)
        if r=="": r= None
        r=float(r)
        if t=="": t= None
        t=float(t)
        assert (p>0 and r>0 and t>0)
        amt=p+(p*r*t/100.0)
        print "The balance amount on Rs.",p,"@",r,"% SI","for",t,"years=",amt
    except TypeError: print sys.exc_info()[0],
    except ValueError as error: print "Value Error",error
    except: print "Not a valid input"          
def compound_int(p,r,t):
    try:
        if p=="": p= None
        print p
        p=float(p)
        if r=="": r= None
        r=float(r)
        if t=="": t= None
        t=float(t)
        assert (p>0 and r>0 and t>0)
        amt=p*(1+r/100.0)**t
        print "The balance amount on Rs.",p,"@",r,"% CI","for",t,"years=",amt
    except TypeError: print sys.exc_info()[0],
    except ValueError as error: print "Value Error",error
    except: print "Not a valid input"
p=raw_input("Enter the principal amount: ")
r=raw_input("Enter the interest rate: ")
t=raw_input("Enter the time period: ")
x=input('''Which type of interest do you want to calculate
Enter 1 for Simple Interest
Enter 2 for Comound Interest: ''')
if x==1: simple_int(p,r,t)
elif x==2: compound_int(p,r,t)
else:print "Invalid Choice"





