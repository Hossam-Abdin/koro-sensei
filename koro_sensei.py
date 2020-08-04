from student_parser import StudentParser
from student_writer import StudentWriter

sp = StudentParser()
sp.filling_basic_data_and_fill_end_term_results()
sp.fill_mid_term_results()
# sp.fill_mid_term_retake_results()
# sp.fill_end_term_retake_results()
# sp.fill_average_hw_and_pt_for_group('group3_FP_evaluations.csv')
sp.fill_average_hw_and_pt_for_group('group2_FP_evaluations.csv')
# sp.fill_average_hw_and_pt_for_group('group1_FP_evaluations.csv')
# sp.fill_quizzes_grades("2020-05-29T2237_Grades-2019_20_2_IP-18fFUNPEG_1_-_Functional_programming_LPr..csv")
# sp.fill_quizzes_grades("2020-05-29T2238_Grades-2019_20_2_IP-18fFUNPEG_2_-_Functional_programming_LPr..csv")
# sp.fill_quizzes_grades("2020-05-29T2238_Grades-2019_20_2_IP-18fFUNPEG_3_-_Functional_programming_LPr..csv")
# sp.fill_theortical_quiz_grades("2020-06-08T1810_Grades-2019_20_2_IP-18fFUNPEG_90_-_Functional_programming_L+Pr..csv")

StudentWriter().write(sp.students)

for s in sp.students:
    print(s.name + " " + s.neptun + " " + str(s.end_term_grade) + " " + str(s.mid_term_grade) + " " + str(s.homewords_grades) + " " + str(s.progress_tasks_grades))