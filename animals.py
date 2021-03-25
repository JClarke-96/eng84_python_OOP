# Creating an Animal class
class Animal():

    # name = "Dog" # class variable
    def __init__(self): # Self refers to the current class
        self.alive = True
        self.spine = True
        self.lungs = True

    def move(self):
        return "Moving left, right, and centre"

    def eat(self):
        return "Keep eating to stay alive"

    def breathe(self):
        return "Keep breathing to stay alive"

# Creating an object of the Animal class
cat = Animal()  # Store all data in Animal in cat
# print(cat.eat())