'''
samosa = int(input("What's your fav number? \n"))
print(samosa)
# if you enter a alpha its gonna show eeror
'''

while True:
    try:
        number = int(input("Whats your fav number bro?\n"))
        print(18/number) # if u enter a 0 its shows error
        print ("Sure")
        break
    except ValueError:
        print("Pls enter a number dude")
    except ZeroDivisionError:
        print("Don't pick zero dick")
    except:
        break
    finally: # a new keyword it says no matter what execute this line of code below
        print("Loop complete")
        