# Többszörös öröklődés
# Azért használjuk, ha egy osztály több osztályból is örököl.


class University:
    def university_info(self):
        return "University"


class Faculty:
    def faculty_info(self):
        return "Faculty"


class Department(University, Faculty):
    def department_info(self):
        return "Department"


department = Department()
print(department.university_info())
print(department.faculty_info())
print(department.department_info())
