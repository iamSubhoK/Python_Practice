class Mario():
    def move(self):
        print('I am moving!')

class Mashroom():
    def eat_mashroom(self):
        print('I ate a Mashroom, Now I am big!')

class BigMario(Mario, Mashroom):
    pass    # if u need a line but u don't want any ocde or anything into it just say pass, and thats it with no errors

bm = BigMario()
bm.move()
bm.eat_mashroom()
