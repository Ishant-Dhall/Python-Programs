#Roman Numbers
print "THE FOLLOWING PRINTS THE ROMAN NUMBER CORRESPONDING TO A DECIMAL NUMBER BETWEEN 1-3000"
x=input("Enter the number: ")
def roman_dig(n,onechar,fivechar,tenchar):
    if n==0: return""
    elif n==1: return onechar
    elif n==2: return onechar*2
    elif n==3: return onechar*3
    elif n==4: return onechar + fivechar
    elif n==5: return fivechar
    elif n==6: return fivechar + onechar
    elif n==7: return fivechar + onechar*2
    elif n==8: return fivechar + onechar*3
    elif n==9: return onechar + tenchar
    else: return
    
        
def roman_num(n):
    return roman_dig( n/1000,'M','','') + roman_dig((n/100)%10,'C','D','M')+ roman_dig((n/10)%10,'X','L','C') + roman_dig(n%10,'I','V','X')
if (x>=0 & x<=3000): num=roman_num(x)
else: print "Out of Range: Enter numbers between 1-3000"
print "The roman number for",x,"is: ",num
