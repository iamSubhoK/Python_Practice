#lists - starts with sq brackets and things can be manipulated inside

subjects = ['physics', 'chemistry', 'maths']
games = ['football', 'cricket', 'tennis']
#things can be done with lists

'''
#append

subjects.append('history')
print(subjects)
'''

'''
# insert

subjects.insert(1, 'history')
print(subjects)
'''

'''
#extends

subjects.extend(games)
print(subjects)
'''

'''
#remove

subjects.remove('chemistry')
print(subjects)
'''

'''
#reverse

subjects.reverse()
print(subjects)
'''

'''
#concatenation

print(subjects + games)
'''

'''
#repetition

print(subjects * 2)
'''

#tuples - starts with parenthesis, data cant be manipulated everythings, data cannto be changed, executes fast than lists

football = ('ronaldo', 'messi', 'rooney')
cricket = ('dhoni', 'virat', 'ashvin')

'''
#append - cant be done on tuples

football.append('kaka')
print(football)

#append cannot be made in tuple as like lists so it shows "error"
'''

'''
#indexing

print(football[1])

print(football.index('rooney'))
'''

'''
#slicing

print(football[0:2])

#not including the last index in slicing
'''

'''
#concatenate

footcrick = football + cricket

print(footcrick) #it adds up the tuples
'''

'''
#repetation

print(football * 2)
'''

'''
#count

print(football.count('ronaldo'))
'''

'''
#length

print(football.__len__())
'''

'''
#just an example

football = [('ronaldo', 'messi', 'rooney'), ('dhoni', 'virat', 'ashvin')]
#inside a list showing two elements

print(football[1][1])
print(football[0][2])
'''

'''
points = [(1,2), (3,4), (5,6)]

#points.append((5,6))

#points.remove((1,2))

print(points)
'''

#strings - can create characters in quotes, can perform multiple operations

chelsea = 'keep the blue flag flying high'

#length
#print(chelsea.__len__())

#index
#print(chelsea.index('b'))

#count
#print(chelsea.count('f'))

#slicing
#print(chelsea[0:7])

#reverse
#print(chelsea[::-1])

#upper all
#print(chelsea.upper())

#multiply
#print(chelsea * 2)

#concatenate
#print(chelsea + " dhinchak pooja ki maa ki choot")

#membership testing
'''
if 'k' in chelsea:
    print('yup bro')
'''

'''
if 'z' not in chelsea:
    print('jdafchysdvgfdfbg')
'''

#sets - contains only unique objects not repeated once, immutable, can perform intersections, unions

integers = {1,2,3,4,5,6,6,6} #the print would not show the repeated elements

#print(integers)

#discard - remove
'''
integers.discard(4)

print(integers)
'''

real = {6,7,8,9,10,11,12}
#added another set

#union - add
#print(integers|real)

#intersection - common elements
#print(integers & real)

#diiference
#print(integers - real)

#symmetric diff
#print(integers ^ real)


#converting a list into a set



dude = [1,2,3,4,5,6,6,6,7,9,10,12]

'''
#its a list with sq brackets

#lets convert it into a set

q = set(dude)

print(q) #all the repeated once get eleminated and converts the list into as set

#lets converty the list into tuple

r = tuple(dude)

print(r) #the list get converted into tuple

'''

#dictionaries - ordered collection of key value pairs, carries huge amount of data
#in curly braaaa

student = {'name':'dude', 'age':25}

'''
print(student['name'])

#lets add another key value
student['gender'] = 'female'

print(student)

'''
#remove a key value
'''
student.pop('age')
print(student)
'''

#clear a dictnary
'''
student.clear()
print(student)
'''
#changing a key value
'''
student['name'] = 'bro'

print(student)
'''
