# Date
date = input("What is the date? (_/_/_) ")

# Student name
name = input("What is your full name? ")

# Student age
age = int(input("How old are you? "))

# Student grade
grade = int(input("What grade are you in? "))

# Student's English result
result1 = float(input("What was your result for English? "))

# Student's Maths result
result2 = float(input("What was your result for Maths? "))

# Student's Science result
result3 = float(input("What was your result for Science? "))

# Student's total score
total = result1 + result2 + result3

# Student's average score
average = total / 3

print("STUDENT EXAMINATION RESULT CARD")
print("Date:", date)
print("Student Name:", name)
print("Student Age:", age)
print("Student Grade:", grade)
print("Student's English score:", result1, "/100")
print("Student's Maths score:", result2, "/100")
print("Student's Science score:", result3, "/100")
print("Student's total score:", total, "/300")
print("Student's average score:", average, "/100")

if average >= 90:
    print("Student's examination grade: A+")
elif average >= 80:
    print("Student's examination grade: A")
elif average >= 70:
    print("Student's examination grade: B")
elif average >= 60:
    print("Student's examination grade: C")
elif average >= 50:
    print("Student's examination grade: D")
else:
    print("Student's examination grade: F")

if average >= 50:
    print("Student's result: PASS")
    print("WELL DONE")
else:
    print("Student's result: FAIL")
    print("KEEP PRACTISING")