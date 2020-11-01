#String Palindrom
ch=raw_input("Enter String:")
l=len(ch)
a=0
flag=0
while a<l:
    if (ch[a])==(ch[l-a-1]):
        flag=1
    a=a+1
if flag==1:
    print "String is Palindrome"
else:
    print "String is not Palindrome"
