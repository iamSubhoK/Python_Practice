#abstract classes - can not be instantiated, can only be ingerited, base class
#it can not directly creeate an object but the data of this class can only be inherited to a
#child clss for in an object

#lets do cal salary

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod

    def calculate_salary(self, sal):

        pass

#lets inherite the abstract class to another class below to cal salary

class Developer(Employee):

    def calculate_salary(self, sal):

        final_salary = sal * 1.10

        return final_salary

    def position_1(self, position):

        self.position = position

        return position

emp_1 = Developer()
print(emp_1.calculate_salary(10000))
print(emp_1.position_1('Web Developer'))

