#without repeating a logic everytime, we use loop for conditions
#of statements or all numbrs of repeatations to perform a task


# 2 types of loops pro-test and pre-test
# in py there is only pre-test loop can be perform

# 3 kinds of loops = while, for, nested


#while - when u dont know how many iterations u required, how many times u need to repeat the task

'''
count = 0

#doina a while with a ocndition
while count < 10: # not including 10
    print("number:", count)
    count += 1

print ("done bro")

'''

#lets do a guessing game using while loop

'''
import random

n = 10
guessed = int(n * random.random()) + 1
#integer type, it genrates a random by random module by plus 1 to exit the
#number from 0 indexing

guess = 0
#initialize a value to it

while guess != guessed: # != not equal
    guess = int(input("new number: "))
    if guess > 0:
        if guess > guessed:
            print("number too large")
        elif guess < guessed:
            print ("number too small")
    else:
        print("sorry, wrong answer")
        break
else:
    print("you made it!")
'''

#for - when u know how many times iterations required

'''
fruits = ['mango', 'apple', 'banana']

for fruit in fruits:
    #giving a range upto the elemnts presents in the list
    print("current fruit:", fruit)

print("done bro")
'''

'''
#lets find a factorial, as we know how many iterations we required
#as factorial takes 4 iterations only

num = int(input("number:"))
factorial = 1

if num < 0:
    print("must be positive") #as we cant calculated factorial for negative values
elif num == 0:
    print("factorial = 1") #if the number is 0 the factorial is always 1
else:
    for i in range(1, num + 1): #the main loop starts here, as if the factorial is grtr
                                #than 1 factorials iterates upto 4 times, as it will keep
                                #on increasing untill the number becomes "num" and
                                #would not include num+1
                                #eg. factorial of 5 is 5*4*3*2*1 = 120
        factorial = factorial * i
print(factorial)

'''


#nested loops - loop inside loop

#lets do a nested while loop for an ATM (auto teller machine "bitch")

'''

print('welcome bro to state bank of bro community ATM')
start = ('Y')
chances = 3 #will get only 3 chances to put correct pin
balance = 50.01
while chances >= 0:
    pin = int(input('please enter your 4 digit pin'))

    if pin == (1234):
        print('you entered your pin correctly\n')
        while start not in ('n', 'NO', 'no', 'N'):
            print('press 1 for your balance\n')
            print('press 2 to make a withdrawl\n')
            print('press 3 to pay in\n')
            print('press 4 to cancel\n')
            option = int(input('what would you like to choose?'))
            if option == 1:
                print('your balance is ',balance,'\n')
                start = input('would you like to go back? ')
                if start in ('n', 'NO', 'no', 'N'):
                    print('thank you')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('how much would you like to withdraw? \n 10/20/30/40/50/60/70/80/90'))
                if withdrawl in [10,20,30,40,50,60,70,80,90]:
                    balance = balance - withdrawl
                    print('\nyour balance is now ', balance)
                    start = input('would you like to go back? ')
                    if start in ('n', 'NO', 'no', 'N'):
                        print('thank you')
                        break
                elif withdrawl != [10,20,30,40,50,60,70,80,90]:
                    print('invalid amount, pls try again')
                    start = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('pls enter desired amount:'))

            elif option == 3:
                pay_in = float(input('how much would you like to pay in? '))
                balance += pay_in
                print('\nyour balance is now ', balance)
                start = input('would you like to go back?')
                if start in ('n', 'NO', 'no', 'N'):
                    print('thank you')
                    break
            elif option == 4:
                print('thank you')
                break
            else:
                print('please enter a correct number. \n')
                start = ('y')
    elif pin != ('1234'):
        print('incorrect pin')
        chances -= 1
        if chances == 0 :
            print('\nno more tries, you may f off')
            break

'''

#lets do nested loop for loop for pythagorean numbers

'''
from math import sqrt
n = int(input('maximal number?'))
for a in range(1, n + 1):
    for b in range(a, n):
        c_sqr = a**2 + b**2
        c = int(sqrt(c_sqr))
        if ((c_sqr - c**2) == 0):
            print(a, b, c)
            
'''

#lets do a bulk reservation for train tickets


'''
travelling = input('yes or no')

while travelling == 'yes':
    num = int(input('number of people travelling'))
    for num in range(1, num +  1):
        name = input("name:")
        age = input("age:")
        sex = input("male or female:")
        print(name, age, sex)

    travelling = input("oops! forgot someone")

'''

