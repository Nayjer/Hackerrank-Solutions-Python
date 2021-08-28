def gradingStudents(grades):
    rounded_grades = [[i, grades[i]+(5-(grades[i]%5))] for i in range(grades_count) if grades[i] >= 38 and grades[i] % 5 in [3, 4]]
    for rounded_grade in rounded_grades:
        grades[rounded_grade[0]] = rounded_grade[1]
    return grades  
