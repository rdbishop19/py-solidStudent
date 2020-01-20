'''
Define a Python class named Student. 
This class will have 5 properties.

First name (string)
Last name (string)
Age (integer)
Cohort number (integer)
Full name (read-only string)
Define getters for all properties.
Define a setter for all but the read only property.
Ensure that only the appropriate value can be assigned to each.
The full name property should return first name and last name 
separated by a space. It's value cannot be set.
'''

class Student:
    
    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0

    @first_name.setter
    def first_name(self, new_name):
        if type(new_name) is str:
            self.__first_name = new_name
        else:
            raise TypeError('First name must be a string')

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return 0

    @last_name.setter
    def last_name(self, new_name):
        if type(new_name) is str:
            self.__last_name = new_name
        else:
            raise TypeError('Last name must be a string')

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Age value must be an integer')
    
    @property
    def full_name(self):
        try:
            return f'{self.__first_name} {self.__last_name}'
        except AttributeError:
            return 0

    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return 0

    @cohort.setter
    def cohort(self, number):
        if type(number) is int:
            self.__cohort = number
        else:
            raise TypeError('Cohort # must be an integer')

    def __repr__(self):
        return f'{self.full_name} is {self.age} years old and in Cohort {self.cohort}.'

kyle = Student()
kyle.first_name = "Kyle"
kyle.last_name = "Cunningham"
# print(kyle.first_name, kyle.last_name)
kyle.age = 33
# print('Age:', kyle.age)
# print('Full Name:', kyle.full_name)
kyle.cohort = 36
# print('cohort:', kyle.cohort)

print(kyle)