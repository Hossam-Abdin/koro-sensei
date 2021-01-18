class Student(object):
    def __init__(self):
        self.name = None
        self.neptun = None
        self.mid_term = None
        self.end_term = None
        self.hw = None
        self.theortical_quiz = None
        self.accepted_pt = None
        self.accepted_quiz = None
    
    def calculate_grade(self):
        if self.end_term is None:
            return None
        if self.end_term < 50:
            return 1
        if self.mid_term < 50:
            return 1
        if self.accepted_pt < 5:
            return 1
        if self.accepted_quiz < 25:
            return 1
        if self.hw/1000 < 0.5:
            return 1
        if self.theortical_quiz < 50:
            return 1
        grade = (self.end_term/100*35 + self.mid_term/100*35 + self.theortical_quiz/100*15 
                + self.hw/1000*15)/100
        if grade < 0.5:
            return 1
        if grade < 0.61:
            return 2
        if grade < 0.71:
            return 3
        if grade < 0.86:
            return 4
        return 5