# HackerRank Grading Students
# Every student receives a grade
# If the difference between the grade and the next multiple of 5 is < 3, round grade up to next multiple of 5
# If the value of the grade is < 38, do not round grade

# Examples:
#
#  grade == 84: round to  (85 - 84 is less than 3)
#  grade == 29: do not round (result is less than 40)
#  grade == 57: do not round (60 - 57 is 3 or higher)
import math

def grading_students(grades):
    for num in range(len(grades)):
        if grades[num] < 38:
            continue

        multiple = math.ceil(grades[num] / 5) * 5

        difference = multiple - grades[num]
        if difference < 3:
            grades[num] = multiple
        else:
            continue

    return grades

print(grading_students([73,67,38,33,66,99]))

