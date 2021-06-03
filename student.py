class Student(object):
    def __init__(self):
        self.name = None
        self.neptun = None
        self.mid_term = -1
        self.end_term = -1
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
        grade = (self.get_percentage())/100
        if grade < 0.5:
            return 1
        if grade < 0.61:
            return 2
        if grade < 0.71:
            return 3
        if grade < 0.86:
            return 4
        return 5

    def get_percentage(self):
        return self.end_term/100*35 + self.mid_term/100*35 + self.theortical_quiz/100*15 + self.hw/1000*15

    def __str__(self):
        return str(self.name) + " " + str(self.neptun) + " " + str(self.end_term) + " " + str(self.mid_term) + " " + str(self.hw) + " " + str(self.accepted_pt) + " " + str(self.accepted_quiz) + " " + str(self.theortical_quiz)