#Polygon area calculator
print "THE FOLLOWING PROGRAM FINDS THE AREA OF A GIVEN POLYGON OR A CIRCLE"
x=input('''Enter 1 for rectangle
Enter 2 for square
Enter 3 for triangle
Enter 4 for a circle: ''')
def rectangle():
        l=input("Enter the length of the rectangle: ")
        b=input("Enter the breadth of the rectangle: ")
        area=l*b*1.0
        print "The area of the rectangle= ",area

def square():
        s=input("Enter the side of the square: ")
        area=s*s*1.0
        print "The area of the square= ",area

def triangle():
        b=input("Enter the base of the triangle: ")
        h=input("Enter the height of the triangle: ")
        area=1/2.0*b*h
        print "The area of the triangle= ",area

def circle():
        r=input("Enter the radius of the circle(in cm): ")
        import math
        area=math.pi*r**2
        print "The area of the circle= ",area
if x==1:rectangle()
elif x==2: square()
elif x==3: triangle()
elif x==4: circle()
else: print "Invalid Choice"


        
