#Reverse String
def reverse(a):
    if a=='':
        return a
    else:
        n=len(a)
        return reverse(a[1:n])+a[0]
a=raw_input("Enter a String:")
print reverse(a)
