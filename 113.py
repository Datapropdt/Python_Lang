#static method: is marked with staticmethod decorator

class Choice:
    def __init__(self, subjects):
        self.subjects = subjects

    @staticmethod
    def validate_subject(subjects):
        if "CSA" in subjects:
            print("this option is no longer available ")
        else:
            return True
            
subjects = ["ds","CSA","FOC","os","toc"]

if all(Choice.validate_subject(i) for i in subjects):
    ch = Choice(subjects)
    print("u have been allotted the : ", subjects)            
