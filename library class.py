#Library class
class Library():
    def __init__(self):
        self.Booknumber=input('Enter the book number')
        self.Name=raw_input('Enter the name of the book')
        self.Author=raw_input('Enter the author of the book')
        self.Publisher=raw_input('Enter the publisher of the book')
        self.price=input('Enter the price of the book') 
        self.Number_of_copies=input('Enter the number of copies')
        self.Number_of_issued_copies=input('Enter the number of copies issued')
    def Display(self):
        print "Book Number:",self.Booknumber
        print "Name of the Book:",self.Name
        print "Author of the Book:",self.Author
        print "Publisher of the Book:",self.Publisher
        print "Price of the Book: ",self.Price
        print "Total no. of copies:",self.Number_of_copies
        print "No. of copies issued:",self.Number_of_issued_copies
    def Checkavailability():
        copies_left=self.Number_of_copies-self.Number_of_issued_copies
        if (copies_left>0):
            print "Book available"
            print "No. of copies available:",self.Number_of_copies 
        elif copies_left==0: print "Book unavailable"
    def Returnbook(self):
        self.Number_of_issued_copies-=1
        self.number_of_copies+=1
    def Issue(self,n):
        self.Number_of_copies-=1
        self.Number_of_copies_issued+=1
lst=[]
n=input('Enter the number of books in the library')
for i in range(0,n):
    book=Library()
    lst.append(book)
for i in range(len(lst)):
    print lst[i]
    

        
