class student:

    perc_rise = 1.05

    def __init__(self, first, last, marks):

        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + '.' + last + '@school.com'

    def fullname(self):

        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):

        self.marks = int(self.marks * 1.05)

class dumb(student):

    perc_rise = 1.10


std_1 = student('neel', 'gandu', 70)
std_2 = student('hemant', 'chutiya', 90)

#for def __init__(self, first, last, marks)

print('{} {}'.format(std_1.first, std_1.last))
print('{} {}'.format(std_2.first, std_2.last))

print(std_1.email)
print(std_2.email)

print(('{} {}'.format(std_1.first, std_1.last)), (std_1.email))
print(('{} {}'.format(std_2.first, std_2.last)), (std_2.email))

#for def fullname(self)

print(std_1.fullname())
print(std_2.fullname())

#for def apply_raise(self) with def fullname(self)

print((std_1.fullname()), (std_1.marks)) #before
std_1.apply_raise()
print((std_1.fullname()),(std_1.marks), "/raise") #after

print((std_2.fullname()), (std_2.marks)) #before
std_2.apply_raise()
print((std_2.fullname()), (std_2.marks), "/raise") #after

#all data as dictionary

#print(student.__dict__)

print(std_1.__dict__)
print(std_2.__dict__)

#for class dumb(student)

std_1 = dumb('neel', 'gandu', 70)

print(std_1.email)
print(std_1.perc_rise)

'''
#this is how python search for class in any program
#for dumb dudes

print(help(dumb))
'''