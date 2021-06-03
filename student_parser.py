import csv
from student import Student

class StudentParser(object):
    def __init__(self, sheets, files):
        self.students = []
        self.sheets = sheets
        self.csv_files = files
    def parse(self):
        for sheet in self.sheets:
            l = self.__reading_csv(sheet)
            self.__get_theory_points_and_info(l)
        for f in self.csv_files:
            l = self.__reading_csv(f)
            self.__get_mid_points(l)
            self.__get_end_points(l)
            self.__get_hw(l)
            self.__get_pt(l)

    def __get_mid_points(self, l):
        for i in range(1, len(l)):
            neptun = l[i][2]
            points = -1
            for j in range(2, len(l[i])):
                if l[0][j].startswith("Mid"):
                    temp_points = l[i][j]
                    if (l[i][j] != "" and points < int(temp_points)):
                        points = int(temp_points)
            for s in self.students:
                if s.neptun == neptun:
                    s.mid_term = points

    def __get_end_points(self, l):
        for i in range(1, len(l)):
            neptun = l[i][2]
            points = -1
            for j in range(2, len(l[i])):
                if l[0][j].startswith("End"):
                    temp_points = l[i][j]
                    if (l[i][j] != "" and points < int(temp_points)):
                        points = int(temp_points)
            for s in self.students:
                if s.neptun == neptun:
                    s.end_term = points
                    break

    def __get_hw(self, l):
        for i in range(1, len(l)):
            neptun = l[i][2]
            hw = 0
            for j in range(2, len(l[i])):
                if l[0][j].startswith("HW"):
                    if (l[i][j] != ""):
                        hw += (int(l[i][j]))
            for s in self.students:
                if s.neptun == neptun:
                    s.hw = hw
                    break

    def __get_pt(self, l):
        for i in range(1, len(l)):
            neptun = l[i][2]
            accepted_pt = 0
            for j in range(2, len(l[i])):
                if l[0][j].startswith("PT"):
                        if (l[i][j] != ""):
                            accepted_pt += (int(l[i][j]))

            for s in self.students:
                if s.neptun == neptun:
                    s.accepted_pt = accepted_pt
                    break
    
    def __get_theory_points_and_info(self, l):
        for i in range(2, len(l)):
            s = Student()
            s.name = l[i][0].strip()
            s.neptun = l[i][2]
            accepted_quiz = 0
            end = 0
            mid = 0
            retake = 0
            for j in range(4, len(l[i])):
                if l[0][j].startswith("Quiz"):
                    if (l[i][j] != ""):
                        accepted_quiz += int(float(l[i][j]))
                if l[0][j].startswith("End"):
                    if(l[i][j] != ""):
                        end = int(float(l[i][j]))
                if l[0][j].startswith("Mid"):
                    if(l[i][j] != ""):
                        mid = int(float(l[i][j]))
                if l[0][j].startswith("Exam"):
                    if(l[i][j] != ""):
                        retake = int(float(l[i][j]))
                
            s.accepted_quiz = accepted_quiz
            s.theortical_quiz = max(mid+end, retake)
            self.students.append(s)

    def __reading_csv(self, f_name):
        with open(f_name, 'rt') as csvfile:
            l = []
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                l.append(row)
        return l        
