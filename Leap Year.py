#WAP to find whether the year is a leap year or not
year=input("Enter the year=")
if year%4==0:
    if year%100==0:
        if year%400==0:
            print year,"is aleap year"
        else:
            print year,"is not aleap year"
    else:
        print year,"is a leap year"
else:
    print year,"is not a leap year"
    
    
