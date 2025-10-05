class students:
    def __init__(self, name, age):
        self.name  = name
        self.age = age

    def student_info(self):
        name_age = f"{self.name} {self.age}"
        return name_age
    
student1 = students("chinedu", 29)
print(student1.student_info())

