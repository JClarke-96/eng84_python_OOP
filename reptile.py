# Import Animal class
from animals import Animal


# Pass Animal class as an argument of Reptile class
class Reptile(Animal):

    def __init__(self):
        super().__init__() # Super is to draw from parent class
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]

    def hunt(self):
        return "Catch the next meal to eat"

    def use_venom(self):
        return "I use if I got?"

    def seek_heat(self):
        return "To stay warm, look for Sun"


reptile_object = Reptile()
# print(reptile_object.hunt())
# print(reptile_object.breathe())
