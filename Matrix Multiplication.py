#Matrix Multiplication
print "THE FOLLOWING PROGRAM TAKES TWO MATRICES FROM THE USER AND PRINTS THEIR PRODUCT IF POSSIBLE"
m=input("Enter the number of rows in 1st matrix: ")
n=input("Enter the number of columns in 1st matrix: ")
p=input("Enter the number of rows in 2nd matrix: ")
q=input("Enter the number of columns in 2nd matrix: ")
if (n!=p):
    print "Number of columns of the first matrix is not equal to the number of rows of the second matrix. Thus can't be multiplied"
else:
    matrix_1=[]
    matrix_2=[]
    product=[]
    print "Enter the first matrix"
    for i in range (0,m):
        matrix_1.append([])
        print "Enter the elements of the",i+1,"row:"
        for j in range (0,n):
            matrix_1[i].append(input(""))
    print "Enter the second matrix"
    for i in range (0,p):
        matrix_2.append([])
        print "Enter the elements of the",i+1,"row:"
        for j in range (0,q):
            matrix_2[i].append(input(""))

for i in range(len(matrix_1)):
   for j in range(len(matrix_2[0])):
       for k in range(len(matrix_2)):
           product[i][j] += matrix_1[i][k] * matrix_2[k][j]
for x in product: print x
