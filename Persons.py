class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def GetFullName(self):
            full_name = self.first_name + self.last_name
            return full_name
        
        
class Student(Person):
    def __init__(self, first_name, last_name, subject_area):
        Person.__init__(self, first_name, last_name)
        self.subject_area = subject_area
    
    def GetStudentInfo(self):
        print("The name of the student is", str(self.first_name), str(self.last_name),
              "and their subject area is", str(self.subject_area))
        

class Teacher(Person):
    def __init__(self, first_name, last_name, course):
        Person.__init__(self, first_name, last_name)
        self.course = course
        
    def GetTeacherInfo(self):
        print("The name of the teacher is", str(self.first_name), str(self.last_name), 
              "and the course they're teaching is", str(self.course))