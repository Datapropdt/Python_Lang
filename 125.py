# multi level inheritance : if a new class derived from a derived class
class person:
    def name(self):
        print(" name: GOPI")

class teacher(person):
    def quali(self):
        print(" qualification ...PhD is must")

class hod(teacher):
    def exper(self):
        print(' experience at least 15 years ')

h = hod() # hod is the object of derived class hod
h.name()
h.quali()
h.exper()
        