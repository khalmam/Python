# HackerLand University has the following grading policy:

#     Every student receives a grade in the inclusive range from 0 to 100.
#     Any grade less than 40 is a failing grade.

#     Any grade that is a multiple of 5 and is 40 or above is a passing grade.

# Sam is a professor at the university and likes to round each student's grade according to these rules:

#     If the difference between the grade and the next multiple of 5 is less than 3, round up to the next multiple of 5.
#     If the value of the grade is less than 38, no rounding occurs as the result will still be a failing grade.
# Examples

# round to
# (85 - 84 is less than 3)
# do not round (result is less than 38)

#     do not round (60 - 57 is 3 or higher)

# Given the initial value of
# for each of Sam's

# students, write code to automate the rounding process.

# Function Description

# Complete the function

# with the following parameter(s):

#     : the grades before rounding

# Returns

#     : the grades after rounding

# Input Format

# The first line contains a single integer,
# , the number of students.
# Each line of the subsequent lines contains a single integer,

# .

# Constraints

#     0 <= grades[i] <= 100

def gradingstudents(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            next_multiple_of_5 = ((grade // 5) + 1) * 5
            if next_multiple_of_5 - grade < 3:
                result.append(next_multiple_of_5)
            else:
                result.append(grade)
    return result

if __name__ == "__main__":
    n = int(input().strip())
    grades = [int(input().strip()) for _ in range(n)]
    final_grades = gradingstudents(grades)
    for grade in final_grades:
        print(grade)