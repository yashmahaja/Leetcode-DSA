a = [1,2,3,4]

print(list(map(lambda x: x**x, a )))


class Bird:
    def move(self):
        print("Bird is flying")

class Fish:
    def move(self):
        print("Fish is swimming")

class FlyingFish(Bird, Fish):
    def special_move(self):
        print("FlyingFish can both fly and swim")

# Object creation
my_flying_fish = FlyingFish()

# Calling methods
my_flying_fish.move()          # Output depends on the MRO
my_flying_fish.special_move()   # Output: FlyingFish can both fly and swim
