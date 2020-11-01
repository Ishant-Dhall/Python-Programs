#book library
loop=1
choice=0
while loop==1:
    print"Book Library"
    print"1.Twilight saga"
    print"2.C++"
    print"3.Calculus"
    print"4.Operational Research"
    print"5.English"
    print"6.Accounts"
    print"7.Python"
    print"8.Java"
    print"9.Information practice"
    print"10.Information Technology"
    print"choose any of the above option"
    choice=int(input("Enter option"))
    if(choice==1):
        print "name of author is AKSHITA GARG"
        print "name of publisher is GARG PUBLISHING HOUSE"
        print "number of copies issued is 10"
        print "number of copies left is 5"
    elif(choice==2):
        print "name of author is DEV KASHYAP"
        print "name of publisher is KASHYAP PUBLISHING HOUSE"
        print "number of copies issued is 8"
        print "number of copies left is 3"
    elif(choice==3):
        print "name of author is AAKASH BANSAL"
        print "name of publisher is BANSAL PUBLISHING HOUSE"
        print "number of copies issued is 15"
        print "number of copies left is 0"
    elif(choice==4):
        print "name of author is DEEPIKA"
        print "name of publisher is Dhanpat Rai"
        print "number of copies issued is 0"
        print "number of copies left is 15"
    elif(choice==5):
        print "name of author is KUMAR ANAND"
        print "name of publisher is ANAND PUBLISHING HOUSE"
        print "number of copies issued is 12"
        print "number of copies left is 3"
    elif(choice==6):
        print "name of author is DINESH DHOLIYA"
        print "name of publisher is DINESH PUBLICATION"
        print "number of copies issued is 15"
        print "number of copies left is 0"
    elif(choice==7):
        print "name of author is HARRY"
        print "name of publisher is HARRY PUBLICATION"
        print "number of copies issued is 5"
        print "number of copies left is 10"
    elif(choice==8):
        print "name of author is KESHAV"
        print "name of publisher is KESHAV PUBLICATION"
        print "number of copies issued is 3"
        print "number of copies left is 12" 
    elif(choice==9):
        print "name of author is ASHISH"
        print "name of publisher is ASHISH PUBLICATION"
        print "number of copies issued is 5"
        print "number of copies left is 10"
    elif(choice==10):
        print "name of author is BHARTI"
        print "name of publisher is SIHAG PUBLICATION"
        print "number of copies issued is 0"
        print "number of copies left is 0"
        print "order 20 books"
    else:
        loop=0
