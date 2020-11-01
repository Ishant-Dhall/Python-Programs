#Factors
print 'THE FOLLOWING PROGRAM FINDS THE FACTORS OF A NUMBER'
x=input('Input the number: ')
n=1
print 'The Factors of',x,'are:'
for n in range(1,(x/2)+1):
    if x%n==0:
        print n
print x
    
