#Class stack
class stack:
    def __init__(self):
        self.values=[]
    def push(self,ele):
        self.values.append(ele)
    def isempty(self):
        if (len(self.values)==0):
            return True
        else:
            return False
    def pop(self):
        if self.values.isempty():
            return None
        else:
            a=self.values.pop()
            return a
    def size_stack(self):
        return len(self.values)
    def top_element(self):
        return (self.values[-1])
    def __str__(self):
        strrep=''
        l=len(self.values)
        for i in range(l-1,-1,-1):
            strrep=strrep+self.values[i]+'\t'
        return strrep
while(True):
    print"""
            1.creating the stack
            2.push operation
            3.check whether stack is empty or not
            4.pop operation
            5.size of stack
            6.top element
            7.display"""
    ch=input("Enter your choice=")
    if ch==1:
        stk=stack()
    elif ch==2:
        element=input("Enter the element=")
        stk.push(element)
    elif ch==3:
        if stk.isempty()==True:
            print"Stack is empty"
        else:
            print"Stack is non empty"
    elif ch==4:
        print stk.pop()
    elif ch==5:
        print stk.size_stack()
    elif ch==6:
        print stk.top_element()
    elif ch==7:
        print stk
    proceed=raw_input("Enter y or Y to continue=")
    if (proceed!='y')and(proceed!='Y'):
        break

    
    
        
