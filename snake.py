# Import reptile class
from reptile import Reptile


class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.limbs = False
        self.venom = True
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return "Smell using tongue"

    def slither(self):
        return "Slither along the floor"

    def shed_skin(self):
        return "Shed skin when they grow"


snake_object = Snake()
# print(snake_object.slither())
# print(snake_object.hunt())
# print(snake_object.eat())