#simple python class with instances
class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position
        self.email = name + "@company.com"

    def stat(self):
        return "{} \n{}".format(self.name,self.position)

emp_1 = Employee("Patrick Diali","Chief Architect,")
emp_2 = Employee("Brutus Beefcake","Web Developer,")

print(emp_1.stat())
mail1 = emp_1.email
print(mail1.replace(' ','')) #strip out spaces in name
print()
print(emp_2.stat())
mail2 = emp_2.email
print(mail2.replace(' ',''))

#this violates DRY
"""emp_1.name = 'Patrick Diali'
emp_1.position = 'Team Lead'
emp_1.email = 'patdiali@company.com'

emp_2.name = 'Mac Aroni'
emp_2.position = 'Snr. Developer'
emp_2.email = 'macaroni@company.com'"""

