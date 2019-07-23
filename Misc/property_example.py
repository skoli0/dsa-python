# @propery example
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first_name, self.last_name)

    # @property
    # def fullname(self):
    #     return '{} {}'.format(self.first_name, self.last_name)
    
    @fullname.setter
    def fullname(self, name):
        self.first_name, self.last_name = name.split()

    # @fullname.deleter
    # def fullname(self):
    #     print('Delete Name!')
    #     self.first_name = 'Empty!'
    #     self.last_name = None

emp = Employee('John', 'Smith')
emp.first_name = 'James'
print(emp.first_name)
print(emp.last_name)
print(emp.fullname)
print(emp.email)

emp.fullname = 'Sandeep Koli'

print(emp.first_name)
print(emp.last_name)
print(emp.fullname)
print(emp.email)
del emp.fullname
print(emp.first_name)
print(emp.last_name)
