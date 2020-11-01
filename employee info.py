#Employee information
class employee:
    def __init__(self,name,job,bsalary,department,project):
        self.name=name
        self.job=job
        self.bsalary=bsalary
        self.department=department
        self.project=project
    def findsalary(self,bsalary):
        da=self.bsalary*0.1
        hra=self.bsalary*0.15
        salary=self.bsalary+da+hra
        self.salary=salary
    def changedepartment(self,newdepartment):
        self.department=newdepartment
    def addproject(self,newproject):
        self.project.append(newproject)
    def __str__(self):
        print 'Name of the employee',self.name
        print 'Department of employee',self.department
        print 'Designation of employee',self.job
        print 'Salary of employee',self.salary
        print 'Project of employee',self.project
        print 'Dearance allowance',self.bsalary*0.1
        print 'Houese rent allowance',self.bsalary*0.15
lst=[]
n=input('Enter the no. of employees')
for i in range(0,n):
    name=raw_input('Enter the name of employee')
    job=raw_input('Enter the designation of employee')
    bsalary=input('Enter the salary of employee')
    department=raw_input('enter the department of employee')
    project=raw_input('Enter the project of employee')
    E1=employee(name,job,bsalary,department,project)
    E1.findsalary(bsalary)
    y=input('do u wanna change anything    1. yes   2.no')
    if y==1:
        x=input('1.change department    2.add project   3. both(1)&(2)    4. None of these')
        if x==1:
            E1.changedepartment=raw_input('enter the new department of employee')
        elif x==2:
            E1.addproject=raw_input('Enter the new project of employee')
        elif x==3:
            E1.department=raw_input('enter the department of employee')
            E1.project=raw_input('Enter the project of employee')
    else:
        pass
    lst.append(E1)
for i in range(len(lst)):
    print lst[i]

        
