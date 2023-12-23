# Animal class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale.")


# Fish class (Extends from "Animal" class)
class Fish(Animal):

    def __init__(self):
        super().__init__()
        
    def breath(self):
        super().breath()
        print("Doing this underwater.")

    def swim(self):
        print("Moving in water.")


# Object creation
nemo = Fish()
nemo.swim()
nemo.breath()
print(f"Number of eyes: {nemo.num_eyes}")
