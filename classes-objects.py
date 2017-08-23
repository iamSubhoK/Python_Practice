class Samosa: #name a class satrting with a caps so that programmers can understand that its a class
    number = 3

    def eat(self):
        print('thats awesome!')
        self.number -= 1

    def check_number(self):
        if self.number <= 0:
            print('Samosas finished')
        else:
            print(str(self.number) + " samosas left")

#to access the stuffs inside a class you need to have object created

samosa1 = Samosa()
samosa2 = Samosa()

samosa1.eat()
samosa1.eat() # we ate 1 + 1 samosa of samosa1
samosa2.eat()
samosa1.check_number()
samosa2.check_number()