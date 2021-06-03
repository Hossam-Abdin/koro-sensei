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
        sheet.write(0, 8, 'Percentage', style)
        sheet.write(0, 9, 'Grade', style)

        i = 1

        for student in students:
            if student.accepted_pt != None:
                sheet.write(i, 0, student.name, style)
                sheet.write(i, 1, student.neptun, style)
                sheet.write(i, 2, student.mid_term, style)
                sheet.write(i, 3, student.end_term, style)
                sheet.write(i, 4, student.hw, style)
                sheet.write(i, 5, student.accepted_pt, style)
                sheet.write(i, 6, student.accepted_quiz, style)
                sheet.write(i, 7, student.theortical_quiz, style)
                sheet.write(i, 8, student.get_percentage(), style)
                sheet.write(i, 9, student.calculate_grade(), style)
                i += 1

        workbook.save("final_grade.xls") 
