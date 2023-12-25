# multi level inheritance : if a new class derived from a derived class
class person:
    def name(self):
        print(" name....")

class teacher(person):
    def quali(self):
        print(" qaulification ...PhD is must")

class hod(teacher):
    def exper(self):
        print(' experience at least 15 years ')

    def all(self):
        self.name()
        self.quali()

hod=hod() # hod is the object of derived class hod

hod.all()
hod.exper()

        
