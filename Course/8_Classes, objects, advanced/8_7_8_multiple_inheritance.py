class Info:
    def get_info(self, info_type):
        if info_type == "university":
            return "University"
        elif info_type == "faculty":
            return "Faculty"
        elif info_type == "department":
            return "Department"
        else:
            return "Unknown Info Type"


info = Info()
print(info.get_info("university"))
print(info.get_info("faculty"))
print(info.get_info("department"))

# Többszörös öröklődés
# Azért használjuk, ha egy osztály több osztályból is örököl.
# Szükségessége az, hogy rugalmassá, olvashatóbbá, bővíthetővé tegyük a kódot.


class Info:
    def university_info(self):
        return "University"


class Faculty:
    def faculty_info(self):
        return "Faculty"


class Department(Info, Faculty):
    def department_info(self):
        return "Department"


department = Department()
print(department.university_info())
print(department.faculty_info())
print(department.department_info())
