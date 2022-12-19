class Student():
    university = "UEK"
    id = 100000

    def __init__(self, name, surname, field):
        self.name = name
        self.surnname = surname
        self.field = field
        self.id = Student.id
        Student.id +=1

    def __str__(self):
        return f"{self.name}, {self.surnname}, ({self.field}), {Student.university}"


student1 = Student("Jan", "Kubiena"< "Informatyka")
print(student1)