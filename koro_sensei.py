from student_parser import StudentParser
from student_writer import StudentWriter

sheets = ["data/2021-06-01T1148_Grades-2020_21_2_IP-18fFUNPEG_90_-_Functional_programming_L+Pr..csv"]
csv_files = ["data/2021-06-03T1117_Grades-2020_21_2_IP-18fFUNPEG_3_-_Functional_programming_L+Pr..csv"]
sp = StudentParser(sheets, csv_files)
sp.parse()
StudentWriter().write(sp.students)
