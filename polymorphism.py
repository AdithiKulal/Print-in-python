class Human:
    def make_sound(self):
        print("I can talk")
class Snake:
    def make_sound(self):
        print("Hiss! Hiss!")
class Dog:
    def make_sound(self):
        print("Woff! Woff!")
class Lion:
    def make_sound(self):
        print("Roar! Roar!!")
def animal_sound(animal):
    animal.make_sound()

human=Human()
snake=Snake()
dog=Dog()
lion=Lion()

animal_sound(human)
animal_sound(snake)
animal_sound(dog)
animal_sound(lion)