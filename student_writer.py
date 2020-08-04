# importing xlwt module 
import xlwt 

class StudentWriter(object):
    
    def write(self, students):  
        workbook = xlwt.Workbook()  
        
        sheet = workbook.add_sheet("Students") 
        
        # Specifying style 
        style = xlwt.easyxf('font: bold 1') 
        
        # Specifying column 
        sheet.write(0, 0, 'Name', style)
        sheet.write(0, 1, 'Neptun', style)
        sheet.write(0, 2, 'Mid-Term', style)
        sheet.write(0, 3, 'End-Term', style)
        sheet.write(0, 4, 'HW', style)
        sheet.write(0, 5, 'PT', style)
        sheet.write(0, 6, 'Quizzes', style)
        sheet.write(0, 7, 'Theortical_quiz', style)
        sheet.write(0, 8, 'can have grade')

        i = 1

        for student in students:
            sheet.write(i, 0, student.name.decode('utf-8'), style)
            sheet.write(i, 1, student.neptun.decode('utf-8'), style)
            sheet.write(i, 2, student.mid_term_grade, style)
            sheet.write(i, 3, student.end_term_grade, style)
            sheet.write(i, 4, student.homewords_grades, style)
            sheet.write(i, 5, student.progress_tasks_grades, style)
            sheet.write(i, 6, student.quizzes_grade, style)
            sheet.write(i, 7, student.theortical_quiz, style)
            if(self.get_can_have_grade(student) == 1):
                sheet.write(i, 8, "passed", style)
            else:
                sheet.write(i, 8, "failed", style)
            i += 1

        workbook.save("final_grade.xls") 

    @staticmethod
    def get_can_have_grade(student):
        if(student.homewords_grades < 50):
            return 0
        if(student.progress_tasks_grades < 50):
            return 0
        if(student.quizzes_grade < 50):
            return 0
        return 1
