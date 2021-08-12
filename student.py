# making a class Teacher and the making multiple objects
from teachers import Teacher
class Students(Teacher):
    def setmarks(self,marks):
        self.marks = marks
    def getmarks(self):
        return self.marks
    
