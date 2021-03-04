# Regular instance method pass instance of class as first argument. eg, self is a reserved keyword which instance of class represent
#class method pass class itself as first argument. It doesn't depend on instance of class
#static method doesn't pass any argument . It doesn't depend on any instance or class

class Players:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return (print(f'Player Name: {self.first} {self.last}'))

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split(',')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

#random csv input variables
emp_str_1 = 'Virat,Kohli,50000'
emp_str_2 = 'Ravi,Ashwin,60000'
emp_str_3 = 'Jasprit,Bumrah,40000'

new_emp_1 = Players.from_string(emp_str_1)         # dont' throw error since 'from_string()' is a class method
new_emp_1.fullname()

import datetime
my_date = datetime.date(2016, 12, 8)
print(Players.is_workday(my_date))
print(my_date.day)