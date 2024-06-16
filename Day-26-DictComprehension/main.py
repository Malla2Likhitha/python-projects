# import random
#
# names = ["Lily", "Beth", "Ali", "JK"]
#
# student_scores = {student: random.randint(50, 100) for student in names}
# print(student_scores)
#
# passed_students = {student: score for (student, score) in student_scores.items() if score > 80}
# print(passed_students)


# weather_c = eval(input())
# # will give dict as input, eval will convert the string input into dict
#
# weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

import pandas

student_scores = {
    'student': ["Lily", "Beth", "Ali", "JK"],
    'score': [75, 68, 53, 73]
}

df = pandas.DataFrame(student_scores)
print(df)
for (index, row) in df.iterrows():
    # print(index)
    # print(row)
    # print(row.score)
    # print(row.student)
    if row.student == 'JK':
        print(row.score)