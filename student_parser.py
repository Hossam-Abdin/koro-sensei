import xlrd
import csv
import re
from student import Student

class StudentParser(object):
    def __init__(self):
        self.students = []

    def filling_basic_data_and_fill_end_term_results(self):
        end_term_book_location = "Endterm Grade Sheet.xlsx"
        end_term_book = xlrd.open_workbook(end_term_book_location) 
        end_term_sheet = end_term_book.sheet_by_index(0)
        for i in range(1, end_term_sheet.nrows):
            s = Student()
            s.name = end_term_sheet.cell(i, 0).value.encode('utf-8').strip()
            s.neptun = end_term_sheet.cell(i, 1).value.encode('utf-8').strip()
            s.end_term_grade = end_term_sheet.cell(i, 2).value
            self.students.append(s)

    def fill_mid_term_results(self):
        mid_term_book_location = "Midterm Grade Sheet.xlsx"
        mid_term_book = xlrd.open_workbook(mid_term_book_location) 
        mid_term_sheet = mid_term_book.sheet_by_index(0)
        for student in self.students:
            for i in range(1, mid_term_sheet.nrows):
                if student.neptun == mid_term_sheet.cell(i, 1).value.encode('utf-8').strip():
                    student.mid_term_grade = mid_term_sheet.cell(i, 2).value
                    break

    def fill_mid_term_retake_results(self):
        mid_term_book_location = "Midterm Retake Grade Sheet.xlsx"
        mid_term_book = xlrd.open_workbook(mid_term_book_location) 
        mid_term_sheet = mid_term_book.sheet_by_index(0)
        for student in self.students:
            for i in range(1, mid_term_sheet.nrows):
                if student.neptun == mid_term_sheet.cell(i, 1).value.encode('utf-8').strip():
                    if mid_term_sheet.cell(i, 2).value > student.mid_term_grade:
                        student.mid_term_grade = mid_term_sheet.cell(i, 2).value
                    break

    def fill_end_term_retake_results(self):
        end_term_book_location = "Endterm Retake Grade Sheet.xlsx"
        end_term_book = xlrd.open_workbook(end_term_book_location) 
        end_term_sheet = end_term_book.sheet_by_index(0)
        for student in self.students:
            for i in range(1, end_term_sheet.nrows):
                if student.neptun == end_term_sheet.cell(i, 1).value.encode('utf-8').strip():
                    if end_term_sheet.cell(i, 2).value > student.end_term_grade:
                        student.end_term_grade = end_term_sheet.cell(i, 2).value
                    break

    def fill_average_hw_and_pt_for_group(self, csv_file_name):

        with open(csv_file_name, 'rb') as csvfile:
            l = []
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                l.append(row)

        for i in range(1, len(l)):
            neptun = l[i][1]
            hw_grades = []
            for j in range(2, len(l[i])):
                if re.search('^"[H-h]', l[0][j]):
                    if (l[i][j] != ""):
                        hw_grades.append(int(l[i][j][:-1]))
                    else:
                        hw_grades.append(0)
            for student in self.students:
                if (student.neptun.strip() == neptun.strip()):
                    student.homewords_grades = (sum(hw_grades) / len(hw_grades))
                    break

        for i in range(1, len(l)):
            neptun = l[i][1]
            pt_grades = []
            for j in range(2, len(l[i])):
                if re.search('^"[P-p]', l[0][j]):
                    if (l[i][j] != ""):
                        pt_grades.append(int(l[i][j][:-1]))
                    else:
                        pt_grades.append(0)
            for student in self.students:
                if (student.neptun.strip() == neptun):
                    student.progress_tasks_grades = (sum(pt_grades) / len(pt_grades))
                    break

    def fill_quizzes_grades(self, csv_file_name):

        with open(csv_file_name, 'rb') as csvfile:
            l = []
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                l.append(row)
                
        for line in l:
            for student in self.students:
                if line[2].strip() == student.neptun.strip():
                    student.quizzes_grade = float(line[23])
                    break

    def fill_theortical_quiz_grades(self, csv_file_name):

        with open(csv_file_name, 'rb') as csvfile:
            i = 0
            l = []
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                if i > 1:
                    l.append(row)
                else:
                    i += 1
                
        for line in l:
            for student in self.students:
                if line[2].strip() == student.neptun.strip():
                    if line[5][:-3] :
                        attemp_2 = int(line[5][:-3])
                    else:
                        attemp_2 = 0
                    if line[4][:-3] :
                        attemp_1 = int(line[4][:-3])
                    else:
                        attemp_1 = 0
                    
                    if (attemp_1 > attemp_2):
                        student.theortical_quiz = attemp_1
                    else:
                        student.theortical_quiz = attemp_2
                    break  

