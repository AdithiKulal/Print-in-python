import random
playing = True #initialise
number = str(random.randint(10,15))
print("I will choose a random number between 10 to 15 and you have to guess it at a time")
print("Let's play!")
while playing:
    guess=input("Enter your guess: ")
    if number==guess:
        print("Nice Guess. You are right!!")
        print("The number is:", number)
        break
    else:
        print("Ohh wrong guess!")
