#     Given the names and grades for each student in a class of  N students, 
# store them in a nested list and 
# print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade,
#  order their names alphabetically and print each name on a new line.
if __name__ == '__main__':

    students = []
            
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    scores = sorted(list(set([student[1] for student in students])))    
    
    
    if len(scores) >= 2 :
        second_lowest_score = scores[1]
        second_lowest_student = sorted([student[0] for student in students if student[1] == second_lowest_score])
    
        for name in second_lowest_student:
            print(name)

    else:
      
        second_lowest_score = scores[0]
        second_lowest_student = sorted([student[0] for student in students if student[1] == second_lowest_score])
    
        for name in second_lowest_student:
            print(name)


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    unique_scores = sorted(list(set([student[1] for student in students])))

    if len(unique_scores) >= 2:
        second_lowest_score = unique_scores[1]
        second_lowest_students = sorted([student[0] for student in students if student[1] == second_lowest_score])
        for name in second_lowest_students:
            print(name)
    elif len(unique_scores) == 1:
        # If there's only one unique score, there's no distinct second lowest.
        # You might want to handle this differently based on the problem's requirements.
        # For now, let's print the names of students with this score.
        lowest_score = unique_scores[0]
        lowest_score_students = sorted([student[0] for student in students if student[1] == lowest_score])
        for name in lowest_score_students:
            print(name)
    else:
        print("No student scores provided.")