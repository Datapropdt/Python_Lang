# static methods : are marked with static method decorator
# it does not use the self variable and is defined using a built in function
# named staticmethod
# using @ decorators is called metaprogramming which a part of the program tries
# to modify another part of program at complile time

class choice:
    def __init__(self, subjects):
        self.subjects = subjects

    @staticmethod  # should be used to define static method
    def validate_subject(subjects):
        if "Tel" in subjects:
            print(" you have been allotted the subjects : ",subjects)
            
        else: print("this option no longer available")
            #return False

subjects = ["Tel","Eng", "phy", "soc", "math"]
if all(choice.validate_subject(i) for i in subjects):
    ch = choice(subjects)

print(" you have been allotted the subjects : ",subjects)
