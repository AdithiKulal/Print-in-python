class Dog:
    animal = "Dog"

    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def display_details(self):
        print("Animal: ",Dog.animal)
        print("Breed: ",self.breed)
        print("Age: ",self.age," years")

dog1 = Dog("Golden Retriever", 3)
dog2 = Dog("German Shepherd", 2)

print("Dog 1 Details:")
dog1.display_details()

print("\nDog 2 Details:")
dog2.display_details()

