class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print("Woof! Woof! I am ",self.name," and I am ",self.age," years old")
    def woof(self):
        print("bow-wow! I am ",self.name," and I am ",self.age," years old")

my_dog=dog("Buddy",5)
my_dog=dog("Teddy",10)

my_dog.bark()
my_dog.woof()