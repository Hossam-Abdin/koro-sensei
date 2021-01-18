from student_parser import StudentParser
from student_writer import StudentWriter

sheets = ["data/LIST90.xlsx", "data/LIST91.xlsx"]
csv_files = ["data/FP group5 Fri 14-16_evaluations.csv", "data/group5.csv"]
sp = StudentParser(sheets, csv_files)
sp.parse()
StudentWriter().write(sp.students)

for s in sp.students:
    print(str(s.name) + " " + str(s.neptun) + " " + str(s.end_term) + 
    " " + str(s.mid_term) + " " + str(s.hw) + " " + str(s.accepted_pt)
    + " " + str(s.accepted_quiz) + " " + str(s.theortical_quiz) + " " + str(s.calculate_grade()))
