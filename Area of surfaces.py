#Area of surfaces
def rec(l,b):
    area=l*b
    return area
def square(side):
    area=side*side
    return area
def circle(r):
    area=(22.0/7.0)*r*r
    return area
def triangle(b,h):
    area=1.0/2.0*b*h
    return area
a=input("Enter 1 for finding area of Rectangle.\nEnter 2 for finding area of Square\nEnter 3 for finding area of Circle\nEnter 4 for finding area of Triangle")
if a==1:
    l=input("Enter length of rectangle:")
    b=input("Enter bredth of rectangle:")
    c=rec(l,b)
    print "Area of Rectangle:",c
elif a==2:
    side=input("Enter side of square:")
    c=square(side)
    print "Area of Square:",c
elif a==3:
    r=input("Enter radius of Circle:")
    c=circle(r)
    print "Area of Circle:",c
elif a==4:
    b=input("Enter Base of Triangle:")
    h=input("Enter Height of Triangle:")
    c=triangle(b,h)
    print "area of Triangle:",c
else:
    print "Wrong Value inserted..."













    
