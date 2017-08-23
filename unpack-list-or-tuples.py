'''
#this is called list
item = ['Aug 13, 2017', 'Bread', 8.51]
'''

'''
#and this is list unpacking, just make sure the number of variable is the number of items in the list
date, name, price = ['Aug 13, 2017', 'Bread', 8.51]

#print
print(name)
'''

#lets put some examples of unpacking of lists
def drop_first_last(grades):
    # not puting grades
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([65, 76, 98, 54, 88])
drop_first_last([76, 98, 90, 76, 33, 76, 89, 67, 76, 55])
