# multi path inheritance
#       student
#         |
#       |----|
#     aca   eca
#       |____|
#       result
class student:
    def name(self):
        print("name ... :gopika ")
class academic_perform(student):
    def acadscore(self):
        print("academic score ... 90% and above ")
class eca(student):
    def ecascore(self):
        print("ECA score ... 60% and above ")
class result(academic_perform,eca):
    def eligibility(self):
        print(" **** min eligible to apply ")
       # self.acad_score()
       # self.eca_score()
r=result()
r.eligibility()
r.acadscore()
r.ecascore()
r.name()

        
