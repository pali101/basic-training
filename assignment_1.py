# Assignment 1 : Gimme the list of all the students that have passed in a class with proper grading system.
#               e.g. if a student has 3 subjects : Math / Physics / Chemistry
#                    if he scores less than 50 % in two of those subjects he fails over all
#                    however if he fails in only 1 subject then he fails in just 1 subject, that should be considered 
#                    as re appear
# 
#               Expectations : 
#                           1. Get a list of students failing in more than 2 or more subjects i.e. overall performance of class
#                           2. Get a list of students failing in 1 subject only - i.e. re appearing student
#                           3. Calculate the overall class performance based on students passed - point #1
#                           4. Calculate the overall performance based on grading system, to showcase the %age of
#                              students falling under 
#                                       a. Distinction - 80 % 
#                                       b. First Division - 60 - 79 % 
#                                       c. Second Division - 50 - 59 %

student1_marks = [54, 77, 93]
student2_marks = [88, 99, 100]
student3_marks = [10, 20, 30]
student4_marks = [10, 50, 50]

all_students = [student1_marks, student2_marks, student3_marks, student4_marks]
pass_student = []
reappear_student = []
failed_student = []

distinction = []
first_division = []
second_division = []
full_marks = 300

#Segregation of students into pass, reappear and fail
for student in all_students:
    counter = 0
    for marks in student:
        if marks < 50:
            counter+=1
    if counter >= 2:
        failed_student.append(student)
    elif counter == 1:
        reappear_student.append(student)
    else:
        pass_student.append(student)


#Overall pass performance
print("Overall performance: ", len(pass_student) * 100 / len(all_students))

#Segregation of passed students into distinction, first class and second class
for student in pass_student:
    total_marks = 0
    for marks in student:
        total_marks += marks

    percent = total_marks * 100 / full_marks
    if percent >= 80:
        distinction.append(student)
    elif percent >= 60 and percent <= 79:
        first_division.append(student)
    else:
        second_division.append(student)



print("Percentage of students with distinction", len(distinction)*100/len(all_students))
print("Percentage of students with first division", len(first_division)*100/len(all_students))
print("Percentage of students with second division", len(second_division)*100/len(all_students))