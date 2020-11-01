#Net Salaey Calculation
print "THE FOLLOWING PROGRAM CALCULATES THE NET SALARY OF AN EMPLOYEE BASED ON HIS BASIC SALARY"
basic_sal=input("Enter the basic salary: ")
da=0.25*basic_sal
if basic_sal>=20000:
    hra=0.12*basic_sal
    ta= 2000
    gross_sal=basic_sal+hra+da+ta
    insur=0.1*gross_sal
elif basic_sal>=10000:
    hra=0.08*basic_sal
    ta= 1000
    gross_sal=basic_sal+hra+da+ta
    insur=0.08*gross_sal
else:
    hra=0.06*basic_sal
    ta= 500
    gross_sal=basic_sal+hra+da+ta
    insur=0.06*gross_sal
pf=0.12*gross_sal
deduc=pf+insur
net_sal=gross_sal-deduc
print "The net salary of the employee is: ",net_sal
