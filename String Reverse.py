#Sring Reverse
print "THE FOLLOWING PROGRAM TAKES A str1ING FROM THE USER AND PRINTS ITS REVERSE"
def reverse(str1):
    if str1=='':
        return str1
    else:
        n=len(str1)
        return reverse(str1[1:n])+str1[0]
def main():
    str1=raw_input("Enter the string: ")
    print reverse(str1)
main()
