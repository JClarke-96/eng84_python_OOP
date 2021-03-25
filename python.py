# Import Snake class
from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def climb(self):
        return "Climb up"

    def chew(self):
        return "Swallow food whole"


python_object = Python()
print(python_object.eat())
print(python_object.hunt())
print(python_object.slither())
print(python_object.chew())