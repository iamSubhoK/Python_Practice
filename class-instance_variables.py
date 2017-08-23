class Bro:

    gender = 'female' #yes i did that

    def __init__(self, name):
        self.name = name #name is need to be unique to each object so use instance variable

r = Bro('Shabnam')
s = Bro('Anamika')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)

#differ variable works dude