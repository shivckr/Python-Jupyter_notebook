class Players:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return (print(f'{self.first} {self.last}'))


emp1 = Players('Ravi', 'Ashwin', 50000)
emp2 = Players('MS', 'Dhoni', 60000)

emp1.fullname()

# Employee.fullname()                 #throw error, can't call instance method by classname, have to pass instance of class as argument

Players.fullname(emp2)

#print(emp1.email)
