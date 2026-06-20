#Date
date=input("What is the date?(_/_/_)")
#Student name
name=input("What is your full name?")
#Student age
age=int(input("How old are you?"))
#Student grade
grade=int(input("What grade are you in?"))
#Student's english result
result1=int(input("What was your result for English?"))
#Student's maths result
result2=int(input("What was your result for Maths?"))
#Student's science result
result3=int(input("What was your result for Science?"))
#Student's toatal score
a=result1+result2+result3
#Student's average score
b=a//3
print("STUDENT EXAMINATION RESULT CARD")
print("Date:",date)
print("Student Name:",name)
print("Student Age:",age)
print("Student Grade:",grade)
print("Student's English score:",result1,"/100")
print("Student's Maths score:", result2,"/100")
print("Student's Science score:", result3,"/100")
print("Student's total score:",a,"/300")
print("Student's average score:", b,"/100")
if b >= 50:
    print("Student's result: PASS")
    print("WELL DONE")
else:
     print("Student's result: FAIL")
     print("KEEP PRACTICING")