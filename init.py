'''
class Samosa:

    def __init__(self): #stands for differentiator or initiator == confused bitch
        print('Awesome!')

    def eat(self):
        print('Feels good!!!')

flipper = Samosa()
flipper.eat()

'''

class Enemy:
    def __init__(self, x): #gonna have enemies with different energy life
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason_b = Enemy(7)
aron_c = Enemy(10)

jason_b.get_energy()
aron_c.get_energy()

