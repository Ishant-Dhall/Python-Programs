#Grade Awarding
print "THE FOLLOWING PROGRAM AWARDS GRADES TO STUDENTS BASED ON THE MARKS OBTAINED BY THEM"
marks=input("Enter the marks obtained by the student (Out of 50): ")
percent=(marks/50.0)*100
if percent>=90: print "Grade A+"
elif percent>=80: print "Grade A"
elif percent>=70: print "Grade B"
elif percent>=60: print "Grade C"
elif percent>=50: print "Grade D"
elif percent>=40: print "Grade E"
else: print "FAIL"
