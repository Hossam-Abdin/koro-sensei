import xlrd
import csv
import re
from student import Student

xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

class StudentParser(object):
    def __init__(self, sheets, files):
        self.students = []
        self.sheets = sheets
        self.csv_files = files
    def parse(self):
        for sheet in self.sheets:
            self.__get_theory_points_and_info(sheet)
        for f in self.csv_files:
            l = self.__reading_csv(f)
            self.__get_mid_points(l)
            self.__get_end_points(l)
            self.__get_hw(l)
            self.__get_pt(l)
            self.__get_quizzes(l)

    def __get_mid_points(self, l):
        for i in range(1, len(l)):
            neptun = l[i][1]
            points = -1
            for j in range(2, len(l[i])):
                if re.search('^"[Mm]', l[0][j]):
                    temp_points = l[i][j][:-1]
                    if (l[i][j] != "" and l[i][j] != "Non-evaluated" and points < int(temp_points)):
                        points = int(temp_points)
            for s in self.students:
                if s.neptun == neptun.encode("utf-8").strip():
                    s.mid_term = points

    def __get_end_points(self, l):
        for i in range(1, len(l)):
            neptun = l[i][1]
            points = -1
            for j in range(2, len(l[i])):
                if re.search('^"[E]', l[0][j]):
                    temp_points = l[i][j][:-1]
                    if (l[i][j] != "" and points < int(temp_points)):
                        points = int(temp_points)
            for s in self.students:
                if s.neptun == neptun.encode("utf-8").strip():
                    s.end_term = points
                    break

    def __get_hw(self, l):
        for i in range(1, len(l)):
            neptun = l[i][1]
            hw = 0
            for j in range(2, len(l[i])):
                if re.search('^"[Hh]', l[0][j]):
                    if (l[i][j] != ""):
                        hw += (int(l[i][j][:-1]))
            for s in self.students:
                if s.neptun == neptun.encode("utf-8").strip():
                    s.hw = hw
                    break

    def __get_pt(self, l):
        for i in range(1, len(l)):
            neptun = l[i][1]
            accepted_pt = 0
            for j in range(2, len(l[i])):
                if re.search('^"[Ppe]', l[0][j]):
                    if (l[i][j] != "" and l[i][j].strip() == "Accepted"):
                        accepted_pt += 1

            for s in self.students:
                if s.neptun == neptun.encode("utf-8").strip():
                    s.accepted_pt = accepted_pt
                    break

    def __get_quizzes(self, l):
        for i in range(1, len(l)):
            neptun = l[i][2]
            accepted_quiz = 0
            for j in range(2, len(l[i])):
                if re.search('^[Qq]', l[0][j]):
                    if (l[i][j] != ""):
                        accepted_quiz += (int(l[i][j]))

            for s in self.students:
                if s.neptun == neptun.encode("utf-8").strip():
                    s.accepted_quiz = accepted_quiz
                    break
    
    def __get_theory_points_and_info(self, sheet):
        book = xlrd.open_workbook(sheet)
        page = book.sheet_by_index(0)
        for i in range(2, page.nrows):
            s = Student()
            s.name = page.cell(i, 0).value.encode('utf-8').strip()
            s.neptun = page.cell(i, 1).value.encode('utf-8').strip()
            mid = 0 if page.cell(i, 2).value == "" else float(page.cell(i, 2).value)
            end = 0 if page.cell(i, 3).value == "" else float(page.cell(i, 3).value)
            retake = 0 if page.cell(i, 4).value == "" else float(page.cell(i, 4).value)
            s.theortical_quiz = max(mid+end, retake)
            self.students.append(s)

    def __reading_csv(self, f_name):
        with open(f_name, 'rt') as csvfile:
            l = []
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                l.append(row)
        return l        
