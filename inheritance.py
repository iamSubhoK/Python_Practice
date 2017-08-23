class Parent():

    def print_last_name(self):
        print('Bro')


class Child(Parent): # we took the details from the parent class that's inheritance

    def print_first_name(self):
        print('BroJr')
'''
    #we gonna understand how to over write the parent last name
    def print_last_name(self):
        print('Dude')
'''
# remove the ''' and see the real dude

brojr = Child()
brojr.print_first_name()
brojr.print_last_name()

