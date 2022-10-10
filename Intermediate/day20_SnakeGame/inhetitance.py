
class Animal:
    def __init__(self):
        self.eye_num = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        # re-initialize this attributes
        self.eye_num = 4

    def breathe(self):
        super().breathe()
        print("doing this under water")

    def swim(self):
        print("Move in the water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(f"Nemo has {nemo.eye_num} eyes")

