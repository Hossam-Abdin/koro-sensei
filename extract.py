# Import:
import xlrd
import csv
import re
# Iterating Over the Number of Rows and Appending to List:

with open('group3_FP_evaluations.csv', 'rb') as csvfile:
    l = []
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        l.append(row)

for student in self.students:
    if (student.neptun.strip() == neptun):
        student.homewords_grades = (sum(hw_grades) / len(hw_grades))
        # print(hw_grades)
        # print(sum(hw_grades))
        # print(len(hw_grades))
        # print((sum(hw_grades) / len(hw_grades)))
        # print(student.name)
        break